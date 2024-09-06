

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

    if n < 1:
        raise ValueError("n should be >= 1")
    else:
        primes = [2, 3, 5, 7]  # we know that 2, 3, 5, 7 are primes
        fibnums = [1, 1]  # fib(0) = 1, fib(1) = 1
        index = 3
        while index < n:
            if fibnums[index - 1] % primes[index - 1] == 0:
                fibnums.append(fibnums[index - 1] + fibnums[index - 2])
                primes.append(primes[index - 1] + 2 * primes[index - 2])
            else:
                fibnums.append(fibnums[index - 1] + fibnums[index - 2])
                primes.append(primes[index - 1] + primes[index - 2])
            index += 1

        return primes[index - 1]

