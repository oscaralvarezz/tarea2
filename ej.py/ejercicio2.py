texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

def transformar(parrafo):
    parrafo = parrafo.replace ("#","\n")
    lineas = parrafo.split("\n")
    for posicion in range(len(lineas)):
        if posicion == 0:
            lineas[posicion] = lineas[posicion].capitalize() + "."
            parrafo = "\n".join(lineas)
            return parrafo

    return transformar(parrafo)