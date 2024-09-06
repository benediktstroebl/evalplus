

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

    # create a list of all prime numbers that are less than or equal to sqrt(n)
    primes = [2, 3]
    test = 5
    while test * test <= n:
        # Check if test is a prime
        isPrime = True
        for prime in primes:
            if test % prime == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(test)
        test += 2

    # compute the fibonacci sequence
    a, b = 1, 2
    seq = [a, b]
    while True:
        # compute the next number in fibonacci sequence
        a, b = b, a + b
        if a >= n:
            break
        seq.append(a)

    # return the n-th number that is a Fibonacci number and it's also prime.
    for i in seq[::-1]:
        for prime in primes:
            if i % prime == 0:
                break
        if i % prime:
            return i

