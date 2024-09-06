

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

    primes = [2, 3]

    fib_n_minus_1 = 0
    fib_n_minus_2 = 1
    fib_n = 1

    while len(primes) < n:
        fib_n_minus_2, fib_n_minus_1 = fib_n, fib_n_minus_1
        fib_n = fib_n_minus_2 + fib_n_minus_1

        for i in range(2, fib_n):
            if fib_n % i == 0:
                break
        else:
            primes.append(fib_n)

    return primes[n - 1]

