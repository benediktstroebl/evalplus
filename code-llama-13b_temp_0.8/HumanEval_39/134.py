

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
    # set first number that's Fibonacci to 2
    fib = [2]

    # set first prime to 2
    primes = [2]

    while len(fib) < n:
        # calculate next fibonacci number
        next_fib = fib[-1] + fib[-2]
        fib.append(next_fib)

        # add all primes
        for i in range(len(fib)):
            # check if fib number is prime
            if (fib[i] > primes[-1]):
                primes.append(fib[i])
                # if it's the n-th prime, return it
                if len(primes) == n:
                    return primes[-1]
    return None

