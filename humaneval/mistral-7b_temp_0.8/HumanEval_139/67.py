
def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """


    #Recebe inteiro n
    n = int(input("Introduz o número inteiro: "))

    #Condição para encontrar o fatorial
    if n == 0:
        return 1
    else:
        #Fatorial de n
        fact = 1
        #Fatorial de n-1
        fact2 = 1
        #Fatorial de n-2
        fact3 = 1

        for i in range(1,n+1):
            fact *= i

        for i in range(1,n):
            fact2 *= i

        for i in range(1,n-1):
            fact3 *= i

        return fact * fact2 * fact3

