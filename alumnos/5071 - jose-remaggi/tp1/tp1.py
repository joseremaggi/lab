#!/usr/bin/python
from utils.help import get_options
from multiprocessing import Process, Queue

def crear_hijos():
    hijos = []

    for i in range(options['hijos']):
        hijo = Process(target=contar_palabras, args=(out_queue,))
        hijos.append(hijo)
        hijo.start()
    return hijos


def contar_palabras(out_queue):
    cantidad_palabras = 0
    while True:
        contenido = in_queue.get()

        if contenido == '':
            break
        longitud_contenido = len(contenido.split())

        cantidad_palabras= cantidad_palabras + longitud_contenido

        out_queue.put(cantidad_palabras)
        if in_queue.empty():
            mostrar_palabras()


def leer_archivo(in_queue):
    import os
    fd = os.open(options['archivo'], os.O_RDONLY)
    delimitadores = [' ', '\t', '\n', ',']
    proxima_palabra = ''
    palabra_parcial = []
    while True:
        contenido = os.read(fd, options['cantidad_bytes'])
        if contenido == '':
            break
        if not contenido[-1] in delimitadores:
            linea_parcial = contenido.split()

            longitud_palabra_parcial = len(linea_parcial[-1])
            palabra_parcial.append(linea_parcial[-1])

            diff = options['cantidad_bytes'] - longitud_palabra_parcial
            if diff != 0:
                palabra_parcial = []
                palabra = proxima_palabra + contenido[0:diff]

                proxima_palabra = contenido[diff: options['cantidad_bytes']]
                in_queue.put(palabra)
            else:
                concatenar_palabra = "".join(palabra_parcial)
                proxima_palabra = proxima_palabra + concatenar_palabra

    os.close(fd)


def mostrar_palabras():
    total_palabras = 0
    while out_queue.qsize() > 0:
        total_palabras = out_queue.get()
	
    print ('Total Palabras encontradas: ', total_palabras)
   

if __name__ == "__main__":
    options = get_options()

    in_queue = Queue()
    out_queue = Queue()

    hijos = crear_hijos()
    
    leer_archivo(in_queue)

    for hijo in hijos:
        hijo.join()
