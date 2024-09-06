

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
    if n <= 0:
        raise ValueError

    # A dict of primes
    primes = {2: True}

    # A dict of Fibonacci numbers
    fibs = {1: True}

    # Iterate till there are enough primes and Fibonacci numbers
    # (each prime is also a Fibonacci number)
    while len(primes) < n and len(fibs) < n:
        # Generate the next Fibonacci number
        last_fib = max(fibs)
        next_fib = last_fib + 1

        # If the next Fibonacci number is prime, add it to primes dict
        for p in range(2, round(next_fib**0.5 + 1)):
            if next_fib % p == 0:
                break
        else:
            primes[next_fib] = True
            fibs[next_fib] = True

        # Generate the next prime number
        last_prime = max(primes)
        next_prime = last_prime + 1
        primes[next_prime] = True

        # If the next prime number is also a Fibonacci number, add it to fibs dict
        for f in fibs:
            if next_prime % f == 0:
                break
        else:
            primes[next_prime] = True
            fibs[next_prime] = True

    # Returns the n-th prime
    if len(primes) < n:
        raise ValueError
    return max(primes)

