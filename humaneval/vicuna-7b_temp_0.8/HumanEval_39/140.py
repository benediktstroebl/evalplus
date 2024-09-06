

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
        return n
    else:
        fib = 0
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        while len(fib) < n:
            if (fib[0] * fib[1]) % n == 0:
                return fib[0]
            if fib[0] in [2, 3]:
                fib.append(fib[0] * fib[1])
            fib.append(fib[0] + fib[1])
        return fib[-1]
