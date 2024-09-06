

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

    if n == 1:
        return 2
    if n == 2:
        return 3
    if n == 3:
        return 5

    primes = [2, 3, 5]

    current_fib = 1
    next_fib = 2

    while len(primes) < n:
        current_fib, next_fib = next_fib, current_fib + next_fib

        for prime in primes:
            if current_fib % prime == 0:
                break
        else:
            primes.append(current_fib)

    return primes[n - 1]

