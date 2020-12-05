# Expresiones Anidadas
print("EXPRESIONES ANIDADAS")
x = 10
# QUEREMOS SABER SI UN NUMERO ESTRA ENTRE 8 Y 10
# Si no cumple nos va a devolver un False
# Si se cumple nos va a devolver un True

# resultado = x>=8 and x<=10
resultado = 8 <= x <= 10
print(resultado)

# Operadores con Asignación
print("OPERADORES CON ASIGNACIÓN")
# En programación se usan muchos los contadores.
# 0
# 0 + 1
# 1
# 1 + 1
# 2

a = 2
print(a)
# a = a + 1
a += 1
print(a)
# a = a + 1
a += 1
print(a)

# Ejercicio
print("Ejericio 1")
# Realizar un programa que lea 2 números por teclado y determine los siguientes
# aspectos (es suficiente con mostrar True o False)
# -Si los dos numeros son iguales (True o False) LISTO
# -Si los dos numeros son diferentes LISTO
# -Si el primero es mayor que el segundo
# -Si el segundo es mayor o igual que primero

n1 = float(input("Introduce el primer número: "))
n2 = int(input("Introduce el primer número: "))

print("¿Son iguales?", n1 == n2)
print("¿Son diferentes?", n1 != n2)
print("¿El primero es mayor que el segundo?", n1 > n2)
print("¿El segundo es mayor o igual que primero?", n2 >= n1)
