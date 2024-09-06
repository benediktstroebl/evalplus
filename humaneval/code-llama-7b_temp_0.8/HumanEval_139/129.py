
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
    list_fact = [1]
    if n > 0:
        for i in range(n):
            if i == 0:
                list_fact.append(list_fact[i])
            else:
                list_fact.append(list_fact[i] * (i))
    return list_fact[n]
