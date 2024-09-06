

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
    # Initialise the list of fibonacci numbers
    fib = [1, 2]
    # Initialise the list of primes
    primes = [2]

    # Calculate the fibonacci numbers and the primes up to the required number
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
        j = 0
        if fib[i] > n:
            return primes[-1]
        while fib[i] >= primes[j] ** 2:
            if fib[i] % primes[j] == 0:
                break
            j += 1
        else:
            primes.append(fib[i])

    # Return the nth prime
    return primes[n]
