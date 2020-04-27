# Con  tu número  de  matrícula  y  tu  nombre,  desarrollauna  gramática  y  un  programa computacional  para
# el  lenguaje  independiente  del  contexto  dado,  que  sea  capaz  de  tomar una cadena de palabras y que
# como resultado indique si la cadena es válida o no para dicha gramática.
#
# Además,debe  dar  la  opción  de  solicitar  otra  cadena  de  entrada  para  analizar,
# hasta que ya no se quiera analizar más cadenas.
#
# L = { i (w)^n i (wI)^(2n)j^2|
# w = las iniciales de tus apellidos,
# i =todos los dígitos de tu número de matrícula,
# wI= w inversa,
# j = tu primer nombre,
# n >= 1 }
# Entonces:
#   w = "ms"
#   i = "1941421"
#   wI = "sm"
#   j = "roberto"


import re

from os import system, name


def clear():

    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


respuesta = "s"

while respuesta == "s" or respuesta == "S":
    nodoble = False
    nodigitos = False
    error = False
    print("Programa para validar cadenas para la gramatica:")
    print("L = { i (w)^n i (wI)^(2n)j^2 |")
    print("w = ms,")
    print("i = 1941421,")
    print("wI = sm,")
    print("j = roberto,")
    print("n >= 1 })")
    print("")
    print("")

    print("Ingrese una cadena para validar: ")
    entrada = input()
    print("")
    entradaSplit = re.split(r"\d+", entrada)

    # print(entradaSplit)

    if len(entradaSplit) > 1:
        wEncontradas = re.findall(r"ms", entradaSplit[1])
        wIEncontradas = re.findall(r"sm", entradaSplit[-1])

        numWEncontradas = len(wEncontradas)
        numWIEncontradas = len(wIEncontradas)

        # print(numWEncontradas, numWIEncontradas)

        if numWIEncontradas == 2 * numWEncontradas:
            cadenaRegex = re.compile(r"(1941421)(ms)+(1941421)(sm)+(roberto){2}")
            mo = cadenaRegex.fullmatch(entrada)
            if mo == None:
                print("Cadena INVALIDA")
                error = True

                # mensajes de errores especificos

            else:
                print("Cadena VALIDA")
        else:
            print("Cadena INVALIDA")
            nodoble = True
            error = True
    else:
        print("Cadena INVALIDA")
        nodigitos = True
        error = True

    cadenaRegex_i = re.compile(r"(1941421)\D+(1941421)\D+")
    mo_i = cadenaRegex_i.fullmatch(entrada)
    cadenaRegex_w = re.compile(r".+(ms)+.+(sm)+.+")
    mo_w = cadenaRegex_w.fullmatch(entrada)
    cadenaRegex_j = re.compile(r".+(roberto){2}")
    mo_j = cadenaRegex_j.fullmatch(entrada)

    if error:
        print("")
        print("ERROES DETECTADOS: ")
        if mo_i == None:
            print("    No se encontraron las matriculas (1941421) de la forma esperada")
        if nodigitos:
            print("    --No se ha encontrado digito alguno en la entrada")
        if mo_w == None or nodoble:
            print(
                "    No se encontraron iniciales de apellidos (ms, sm) de la forma esperada"
            )
        if nodoble:
            print("    --El numero de repeticiones de 'sm' no es el doble de 'ms'")
        if mo_j == None:
            print("    No se ha encontrado el nombre (roberto) de la forma esperada")
    print("")
    print("¿Desea validar otra cadena? (s/n)")

    respuesta = input()

    while (
        respuesta != "s" and respuesta != "n" and respuesta != "S" and respuesta != "N"
    ):
        clear()
        print("Programa para validar cadenas para la gramatica:")
        print("L = { i (w)^n i (wI)^(2n)j^2 |")
        print("w = ms,")
        print("i =1941421,")
        print("wI= sm,")
        print("j = roberto,")
        print("n≥ 1 })")
        print("")
        print("")
        print("Respuesta no reconocida")
        print("")
        print("¿Desea validar otra cadena? (s/n)")
        respuesta = input()
    clear()

print("Fin del programa: presione cualquier tecla...")
tecla = input()
clear()
