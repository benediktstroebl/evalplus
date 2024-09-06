

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

    if n <= 1:
        return 2

    if n == 2:
        return 3

    if n > 2:
        i = 3
        result = 5
        while i < n:
            # Fibonacci sequence
            result = (i + 1) * result - result // i
            # Primes
            if result > 1 and not any(result % p == 0 for p in range(2, int(result ** 0.5) + 1)):
                return result
            i += 1
