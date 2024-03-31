""" 
1. Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

2. Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

3. Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

4. Crear una función que convierta entre grados Celsius, Farenheit y Kelvin
Fórmula 1 : (°C × 9/5) + 32 = °F
Fórmula 2 : °C + 273.15 = °K
Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino

Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo"""
def primo(n):
    if type(n) != int:
        return None
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def lista_primo(list_values):
    primo_list = []
    if list_values == []:
        return "List without values"
    if type(list_values) != list:
        return None
    for value in list_values:
        if primo(value) == True:
            primo_list.append(value)
        else:
            pass
    return primo_list

def contador_numeros(lista_numeros):
    repetidos = {}
    if type(lista_numeros) != list:
        return None
    for i in lista_numeros:
        if type(i) not in (int, float):
            return None
    for value in lista_numeros:
        if value not in repetidos:
            repetidos[value] = 1
        else:
            repetidos[value] += 1
    repetidos_ordenados = dict(sorted(repetidos.items(), key= lambda item:item[1], reverse=True))
    num, times = next(iter(repetidos_ordenados.items()))
    return f"Uno de los valores más repetidos fue {num}, y se repitió {times} veces"


def conversor_temperature(value= 0.0, start="", end=""):
    """
    Value: can be type int or float
    start: [C, F, K]
    end: [C,F,K]
    you can select what type of temperature (start) do you need to convert (end)
    """
    try:
        if type(start) != str or type(end) != str:
            return None
        if start.upper() == "C":
            if end.upper() == "F":
                return f"De Celsius a Farenheit es: {round(value*9/5 + 32, 3)}"
            elif end.upper() == "C":
                return f"De Celsius a Celsius es: {round(value, 3)}"
            elif end.upper() == "K":
                return f"De Celsius a Kelvin es: {round(value + 273.15,3)}"
            else:
                return None
        elif start.upper() == "F":
            if end.upper() == "F":
                return f"De Farenheit a Farenheit es: {round(value, 3)}"
            elif end.upper() == "C":
                return f"De Farenheit a Celsius es: {round((value-32)*5/9, 3)}"
            elif end.upper() == "K":
                return f"De Farenheit a Kelvin es: {round((value-32)*5/9 + 273.15, 3)}"
            else:
                return None
        elif start.upper() == "K":
            if end.upper() == "F":
                return f"De Kelvin a Farenheit es: {round((value-273.15)*9/5 + 32, 3)}"
            elif end.upper() == "C":
                return f"De Kelvin a Celsius es: {round(value-273.15, 3)}"
            elif end.upper() == "K":
                return f"De Kelvin a Kelvin es: {round(value, 3)}"
            else:
                return None
        else:
            return None
    except (SyntaxError, ValueError, KeyError, TypeError) as e:
        return e
