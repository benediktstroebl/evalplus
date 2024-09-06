

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

    fib = 1
    fib_previous = 0
    num = 0
    while fib < n:
        num = fib_previous + fib
        fib_previous = fib
        fib = num
    if num > 1:
        i = 2
        while i <= num ** 0.5:
            if num % i == 0:
                break
            i += 1
        else:
            return num
    return num

