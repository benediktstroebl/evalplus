

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
    fib = [1, 1]
    while len(fib) < n + 1:
        fib.append(fib[-1] + fib[-2])
    fib = fib[1:]
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for p in primes:
        if p > fib[-1]:
            return fib[-1]
        if p not in fib:
            continue
        i = fib.index(p)
        if i < len(fib) - 1:
            return fib[i + 1]

