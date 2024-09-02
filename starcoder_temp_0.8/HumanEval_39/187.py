

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
    k = 0
    while True:
        nth = fib(k)
        if is_prime(nth):
            if k == n:
                return nth
            else:
                k += 1
        else:
            k += 1
