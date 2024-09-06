

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """

    fib1 = 1
    fib2 = 2
    nth_fib = 3
    while nth_fib < n:
        nth_fib = fib1 + fib2
        fib1 = fib2
        fib2 = nth_fib
    nth_fib -= 1
    while nth_fib > 1:
        if nth_fib % fib2 == 0:
            nth_fib -= 1
            continue
        else:
            break
    if nth_fib == 1:
        return nth_fib
    else:
        return fib1

