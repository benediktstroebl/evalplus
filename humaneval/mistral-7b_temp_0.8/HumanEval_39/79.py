

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
    from math import sqrt, floor

    if n < 3:
        return n

    primes = [2, 3]

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            break
        else:
            primes.append(i)

    for i in range(2, floor(sqrt(n)) + 1):
        if i not in primes:
            continue

        for j in range(2, floor(sqrt(n)) + 1):
            if j not in primes:
                continue

            if i + j == n:
                return n

    return n

