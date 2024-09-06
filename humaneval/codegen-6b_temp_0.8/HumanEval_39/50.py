

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
    if n < 0:
        raise Exception("no negative values")

    if n == 1:
        return 2

    fib1 = 1
    fib2 = 1
    i = 3
    while i <= n:
        temp = fib2
        fib2 = fib1 + fib2
        fib1 = temp
        i += 1

    # if fib2 is not prime, find next prime
    i = temp
    while is_prime(i) is not True:
        i += 2

    return i

