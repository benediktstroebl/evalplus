

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
    def is_prime(x: int):
        if x <= 1:
            return False
        if x <= 3:
            return True
        if x % 2 == 0 or x % 3 == 0:
            return False
        i = 5
        while i * i <= x:
            if x % i == 0 or x % (i + 2) == 0:
                return False
            i += 6
        return True

    fib_cache = [0, 1]

    def fib(n):
        while n >= len(fib_cache):
            fib_cache.append(fib_cache[-1] + fib_cache[-2])
        return fib_cache[n]

    i = 1
    while not is_prime(fib(i)):
        i += 1

    return fib(i)

