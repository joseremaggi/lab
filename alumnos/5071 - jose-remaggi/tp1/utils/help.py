import argparse


def get_options():
    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('-f', '--archivo', dest="archivo", required=True, help='Ingresar nombre del archivo.')
    parser.add_argument('-n', '--cantidad_bytes', dest="cantidad_bytes", required=True, type=int,
                        help='Ingresar cantidad de bytes a leer del archivo.')
    parser.add_argument('-p', '--processes', dest="hijos", default=2, type=int,
                        help='Ingrese cantidad de hijos.')

    options = {
        'archivo': parser.parse_args().archivo,
        'cantidad_bytes': parser.parse_args().cantidad_bytes,
        'hijos': parser.parse_args().hijos
    }

    return options
