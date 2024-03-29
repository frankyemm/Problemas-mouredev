"""Problema 1* fizzbuzz
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 *

 """
 for i in range (1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0 and not i % 5 ==0:
        print("fizz")
    elif not i % 3 == 0 and i % 5 ==0:
        print("buzz")
    else:
        print(i)
"""Problema 2* anagrama
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 *
 """
def anagrama(string1, string2):
    dict1 = {}
    dict2 = {}
    for i in string1:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1
    for j in string2:
        if j not in dict2:
            dict2[j] = 1
        else:
            dict2[j] += 1  
    if dict1 == dict2:
        return True
    else:
        return False
"""Problema 3* fibonacci
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13... 
"""
def fibonacci(n):
    counter = 0
    fibopas = 0
    fibopre = 1
    fibof = 1
    print(f"0\n1")
    if counter <= n:
        for i in range(1, n-1):
            print(fibof)
            fibopas = fibopre
            fibopre = fibof
            fibof = fibopas + fibopre
"""Problema 4* es primo
*Escribe un programa que se encargue de comprobar si un número es o no primo.
* Hecho esto, imprime los números primos entre 1 y 100.
*
"""
def primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
"""Problema 5* área del polígono
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
"""
def area(p, a):
    try:
        result = float(p)*float(a)/2
        return result
    except ValueError:
        return "el valor no es permitido"
print("Recuerda que el perímetro es la suma de los lados y, que la apotema es la distancia que hay desde el centro de uno de sus lados hasta el centro de la figura")
p = input("ingrese el perímetro de la figura: ")
a= input("ingrese la apotema de la figura: ")
print(area(p,a))
"""Problema 7* invertir cadena
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""
def invertir(string):
    return string[::-1]
"""Problema 8* contador de palabras
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
"""
def counterword(string):
    alphabet = {"A": "a","B": "b","C": "c","D": "d","E": "e","F": "f","G": "g","H": "h","I": "i","J": "j","K": "k","L": "l","M": "m","N": "n","O": "o","P": "p","Q": "q","R": "r","S": "s","T": "t","U": "u","V": "v","W": "w","X": "x","Y": "y","Z": "z"}
    symbol = [".", ",", ":", ";", "?", "!", "-", "'", "\"", "(", ")", "[", "]", "{", "}", "/", "\\", "<", ">"]
    string_formated = ""
    new_word = ""
    words = {}
    total_words = 0
    for letter in string+".":
        if letter in symbol:
            letter = " "
        if letter in alphabet:
            letter = alphabet[letter]
        string_formated += letter
    
    for char in string_formated:
        if char != " ":
            new_word += char
        else:
            if new_word:
                if new_word not in words:
                    words[new_word] = 1
                else:
                    words[new_word] += 1
                new_word = ""
    for i in words:
        print(i, words[i])
        total_words += words[i]
    return print(f"Hay un total de {total_words} palabras")
"""Problema 9* de decimal a binario
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 *
"""
def decBin(number):
    number_string = ""
    while number > 1:
        number_string += str(number % 2)
        number = number//2
    return "1"+number_string[::-1]
"""Problema 10* conversion morse_natural
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
 *
"""
def conv(text):
    en_alphabet = {"A": ".-","B": "-...","C": "-.-.","D": "-..","E": ".","F": "..-.","G": "--.","H": "....","I": "..","J": ".---","K": "-.-","L": ".-..","M": "--","N": "-.","O": "---","P": ".--.","Q": "--.-","R": ".-.","S": "...","T": "-","U": "..-","V": "...-","W": ".--","X": "-..-","Y": "-.--","Z": "--..","0": "-----","1": ".----","2": "..---","3": "...--","4": "....-","5": ".....","6": "-....","7": "--...","8": "---..","9": "----.",".": ".-.-.-",",": "--..--","?": "..--..","'": ".----.","!": "-.-.--","/": "-..-.","(": "-.--.",")": "-.--.-","&": ".-...",":": "---...",";": "-.-.-.","=": "-...-","+": ".-.-.","-": "-....-","_": "..--.-","\"": ".-..-.","$": "...-..-","@": ".--.-.", " ": "       "}
    conversion = ""
    text = text.upper()
    try:
        if not all(char in '. -' for char in text):
            for char in text:
                conversion += en_alphabet[char]+ " "
            return print(f"Natural to morse is: \n{conversion}")
        else:
            inverted_dict = {value: key for key, value in en_alphabet.items()}
        for item in text.split():
            conversion += inverted_dict[item] + " "
        return print(f"Morse to natural is: \n{conversion}")
    except (ValueError, KeyError, IndexError, SyntaxError) as e:
        return print("An error has occurred: ", e) 
"""Problema 11* comprobar ecuación balanceada
 * Crea un programa que comprueba si los paréntesis, llaves y corchetes
 * de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran
 *   en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios.
 *   No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 *
"""
def balanced(expresion):
    sqr_b = ""
    par = ""
    curl_b = ""
    try:
        expresion = str(expresion)
        if expresion.count("[") == expresion.count("]"):
            sqr_b += "Square bracket are balanced"
        else:
            sqr_b += "Square bracket aren't balanced"
        if expresion.count("(") == expresion.count(")"):
            par += " Parentheses are balanced"
        else:
            par += " Parentheses aren't balanced"
        if expresion.count("{") == expresion.count("}"):
            curl_b += " Curl bracket are balanced"
        else:
            curl_b += " Curl bracket aren't balanced"
        return sqr_b, par, curl_b
    except (KeyError, ValueError, TypeError, SyntaxError) as e:
        return e
"""Problema 12* en uno sí y en otro no str
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
 *
"""
def chains(str1, str2):
    out1 = ""
    out2 = ""
    for i in str1:
        if i not in str2:
            out1 += i
    for j in str2:
        if j not in str1:
            out2 += j
    return out1, out2
"""Problema 13* palíndromo
 * Escribe una función que reciba un texto y retorne verdadero o
 * falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee
  * de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
 *
"""
def palindrome(text):
    symbol = [".", ",", ":", ";", "?", "!", "-", "'", "\"", "(", ")", "[", "]", "{", "}", "/", "\\", "<", ">"]
    text = text.split()
    new_text = "".join(text)
    joined = ""
    for char in new_text:
        if char in symbol:
            char = ""
        joined += char
    if joined == joined[::-1]:
        return True
    else:
        return False
"""Problema 14* factorial recursivo
 * Escribe una función que calcule y retorne el factorial de un número dado
 * de forma recursiva.
 *
"""
def recursived_factorial(n):
    try:
        n = int(n)
        if n == 1 or n == 0:
            return 1
        if 0 < n < 1 or n < 0:
            return "Please enter a int value >= 0"
        if n > 1:
            return n*recursived_factorial(n-1)
    except (KeyError, TypeError, ValueError, SyntaxError) as e:
        return e
"""Problema 15* número narcisista
 * Escribe una función que calcule si un número dado es un número de Armstrong
 * (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información
 * al respecto.
 *
"""
def narcisist(n):
    sum = 0
    for i in str(n):
        i = int(i)
        sum += i**len(str(n))
    if sum == int(n):
        return True
    else:
        return False
"""Problema 16*
 * Crea una función que calcule y retorne cuántos días hay entre dos cadenas
 * de texto que representen fechas.
 * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 * - La función recibirá dos String y retornará un Int.
 * - La diferencia en días será absoluta (no importa el orden de las fechas).
 * - Si una de las dos cadenas de texto no representa una fecha correcta se
 *   lanzará una excepción.
 *
"""
