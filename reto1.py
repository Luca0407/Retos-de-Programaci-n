"""
EJERCICIO:
- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
  Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
  (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
  que representen todos los tipos de estructuras de control que existan
  en tu lenguaje:
  Condicionales, iterativas, excepciones...
- Debes hacer print por consola del resultado de todos los ejemplos.

DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""

# Ej 1:
import time


a = 6
b = 3
c = True
d = [1, 2, 4, 5, 6, 7, 8, 9, 0]
e = input("ingresar valor\n> ")
f = 0

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
modulo = a % b
exponente = a ** b
div_entera = a // b

print("Operadores Aritméticos:")

print("suma: ", suma)
print("resta: ", resta)
print("multiplicación: ", multiplicacion)
print("división: ", division)
print("modulo: ", modulo)
print("exponente: ",exponente)
print("división entera: ", div_entera)

igual_a = a == b
desigual_a = a != b
mayor_que = a > b
menor_que = a < b
mayor_igual = a >= b
menor_igual = a <= b

print("Operadores de Comparación:")

print("igual a:", igual_a)
print("desigual a:", desigual_a)
print("mayor que:", mayor_que)
print("menor que:", menor_que)
print("mayor o igual a:", mayor_igual)
print("menor o igual a:", menor_igual)

asignacion = "="
suma_compuesta = "+=" 
resta_compuesta = "-="
mult_compuesta = "*="
div_compuesta = "/="
modulo_compuesto = "%="

print("Operadores de Asignación y Asignación Compuesta:")

print("asignación: ", asignacion)
print("suma compuesta: ", suma_compuesta)
print("resta compuesta: ", resta_compuesta)
print("multiplicación compuesta: ", mult_compuesta)
print("división compuesta: ", div_compuesta)
print("modulo compuesto: ", modulo_compuesto)

y = a and b >= 1
o = a > 5 or b > 5
no = not c

print("Operadores Lógicos:")

print("y: ", y)
print("o: ", o)
print("no: ", no)

es = a is b
no_es = a is not b

print("Operadores de Identidad:")

print("es: ", es)
print("no es:", no_es)

en = a in d
no_en = b not in d

print("Operadores de Pertenencia:")

print("en: ", en)
print("no en: ", no_en)

y_bit = b > 2 & a in d 
o_bit = a > 2 | b > 2
xor = a ^ b
not_bit = ~ b
desp_izquierda = a << b
desp_derecha = 8 >> b

print("Operadores de Bits:")

print("y de bits: ", y_bit)
print("o de bits: ", o_bit)
print("xor: ", xor)
print("not de bits: ", not_bit)
print("desplazamiento izquierda: ", desp_izquierda)
print("desplazamiento derecha: ", desp_derecha)

# Ej 2:
if (a > b):
    print(f"{a} es mayor que {b}")
elif (b > a):
    print(f"{b} es mayor que {a}")
else:
    print(f"{a} es igual a {b}")

match e:
    case "a":
        print("es a")

    case "b":
        print("es b")
 
    case other:
        print("no es a ni b")

for nums in d:
    if nums == a:
        continue

    print(nums)

while f != 10:
    if f != 5:
        print(f)
        f += 1
    else:
        break

#EXTRA
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
        time.sleep(0.2)
    else:
        continue
