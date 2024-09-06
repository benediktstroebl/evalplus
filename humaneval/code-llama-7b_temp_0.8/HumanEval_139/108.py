
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

    fatoriais = []

    for i in range(n):
        fatoriais.append(i)

    fatoriais = fatoriais[::-1]
    fatoriais_final = []

    for i in fatoriais:
        fatoriais_final.append(i*fatoriais[fatoriais.index(i) - 1])

    fatoriais_final = fatoriais_final[::-1]
    fatoriais_final.pop(0)
    fatoriais_final.pop(0)
    fatoriais_final.pop(0)

    total = 1
    for i in fatoriais_final:
        total *= i

    return total

