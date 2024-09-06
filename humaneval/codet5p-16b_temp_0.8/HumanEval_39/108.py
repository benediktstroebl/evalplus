

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

    primes = [2, 3, 5, 7, 11]
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
        if len(fib) % 2 == 0:
            continue
        elif len(fib) % 2 == 1:
            if fib[-1] in primes:
                continue
            else:
                break
    return fib[-1]

