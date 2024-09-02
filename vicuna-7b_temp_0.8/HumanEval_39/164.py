

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
    n = int(n)

    if n <= 1:
        return n

    for x in range(2, int(n/2)+1):
        if n % x == 0:
            return x
        if x > 2:
            if prime_fib(x) == n:
                return x
            if prime_fib(x-1) == n:
                return x

    if n > 2:
        if is_prime(n-1) or is_prime(n-2):
            return n-1 or n-2