
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

    # fact = n
    # fact_list = [fact]
    # while n >= 2:
    #     fact *= (n-1)
    #     fact_list.append(fact)
    #     n -= 1
    # print(fact_list)
    # return fact

    # answr = 1
    # for n in range(n):
    #     answr *= n
    #     answr *= n+1
    # return answr

    # return functools.reduce(lambda x, y: x*y, range(1, n+1)) * functools.reduce(lambda x, y: x*y, range(1, n))

    # return functools.reduce(lambda x, y: x*y, range(1, n+1)) * functools.reduce(lambda x, y: x*y, range(1, n-1))

    # return functools.reduce(lambda x, y: x*y, range(1, n+1)) * functools.reduce(lambda x, y: x*y, range(1, n-1))

    # return functools.reduce(lambda x, y: x*y, range(1, n+1)) * functools.reduce(lambda x, y: x*y, range(1, n-1))

    # return functools.reduce(lambda x, y: x*y, range(1, n+1)) * functools.reduce(lambda x, y: x*y, range(1, n-1))

    # return functools.reduce(lambda x, y: x*y, range(1, n+1)) * functools.reduce(lambda x, y: x*y, range(1, n-1))

    return functools.reduce(lambda x, y: x*y, range(1, n+1)) * functools.reduce(lambda x, y: x*y, range(1, n))
