

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # 3 lines: pep8
    #fib1, fib2 = 1, 1
    #for _ in range(n-1):
        #fib1, fib2 = fib2, fib1+fib2
        #return fib2

    # 3 lines: pep8
    #a, b = 1, 1
    #for _ in range(n-1):
        #a, b = b, a+b
    #return b

    # 2 lines: pep8
    #fib1, fib2 = 1, 1
    #for _ in range(n-1):
        #fib1, fib2 = fib2, fib1+fib2
    #return fib2

    # 2 lines: pep8
    #a, b = 1, 1
    #for _ in range(n-1):
        #a, b = b, a+b
    #return b

    # 1 line: pep8
    return (1, 1) [n < 1] + fib(n-1) + fib(n-2)

