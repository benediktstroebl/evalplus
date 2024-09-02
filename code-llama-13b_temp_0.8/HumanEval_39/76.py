

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
    # 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
    if n <= 0:
        return 0
    if n == 1:
        return 2

    fib1 = 1
    fib2 = 1
    while n > 1:
        temp = fib2
        fib2 = fib1 + fib2
        fib1 = temp
        if is_prime(fib2):
            n -= 1

    return fib2

