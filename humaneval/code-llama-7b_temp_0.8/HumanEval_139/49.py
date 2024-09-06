
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
    special = []
    for i in range(n):
        special.append(i)
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        for i in range(n-1):
            special = special[:-1]
            print(special)
        print(special)
        return special[0] * special_factorial(len(special))
