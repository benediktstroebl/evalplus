

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
    # fib(0) = 2, fib(1) = 1
    fib = [2, 1]
    # create a set for storing all fibonacci numbers already found
    fib_set = set([1, 2])
    # create a set of primes
    prime_set = set([2])

    k = 3
    while k <= n:
        fib.append(fib[k - 2] + fib[k - 1])
        fib_set.add(fib[k])
        if fib[k] % 2 == 0:
            k += 2
            continue
        i = 3
        temp_fib = fib[k - 1] + fib[k - 2]
        while temp_fib % i != 0:
            i += 2
        prime_set.add(i)
        k += 2
    return (fib[n - 1], list(fib_set), list(prime_set))

