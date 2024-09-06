

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
    # Initialize fibonacci list
    # First prime is 2, first Fibonacci is 0, so we start from the second element
    fib = [0, 1]
    # Initialize a counter for primes
    primes = [2]
    # Iterate until fib reaches n-th number
    while len(fib) <= n:
        # Add next Fibonacci number
        fib.append(fib[-1] + fib[-2])
        # Check if it is prime
        for prime in primes:
            if fib[-1] % prime == 0:
                break
        else:
            primes.append(fib[-1])
    # If n is bigger than prime number counter, then we don't have prime Fibonacci number
    if n > len(primes):
        raise ValueError("There is no {}-th prime-Fibonacci number.".format(n))
    return primes[n - 1]

