
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # a = int(input("Escriba un numero: "))
    if a < 100:
        lista = []
        for i in range(2, a):
            for j in range(2, i):
                if (i % j == 0):
                    break
                else:
                    lista.append(i)
        print(lista)
        print(a * lista[0] * lista[1])

