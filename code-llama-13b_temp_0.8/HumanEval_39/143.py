

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
    fib = [0, 1, 1]

    def is_prime(n):
        for i in range(2, int(n**.5) + 1):
            if n % i == 0:
                return False
        return True

    i = 3
    while len(fib) < n:
        if is_prime(i):
            fib.append(i)
        i += 1
    return fib[n]

