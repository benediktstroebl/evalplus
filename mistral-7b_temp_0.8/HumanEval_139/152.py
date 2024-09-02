
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
    # inicia um contador com 0
    # essa função só funciona para n > 0
    # multiplica o n! pelo n-1! pelo n-2! pelo 1!
    # 1! = 1
    # primeiro coloca 1 na variavel c
    # inicializa a variavel total com 1
    # enquanto o contador for menor que o n, o contador vai se tornando maior que o anterior
    # isso irá fazer a contagem de 0 para n
    # em cada contador, a variavel c vai receber o valor de c * (n - contador)!
    # o valor de n começa no 1
    # o resultado total vai sendo atualizado para cada c * (n - contador)!
    c = 1
    total = 1
    contador = 0
    while contador < n:
        contador = contador + 1
        c = c * (n - contador)
        total = total * c
    return total
