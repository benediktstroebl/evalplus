

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

    
    def is_prime(n: int):
        if n < 2:
            return False
        if n % 2 == 0:
            return n == 2
        k, q = 3, n ** 0.5
        while k <= q:
            if n % k == 0:
                return False
            k += 2
        return True

    def fib(n: int):
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    f = fib(n)
    p = is_prime(f)
    while p is False:
        f += 1
        p = is_prime(f)
    return f

