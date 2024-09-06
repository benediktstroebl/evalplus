

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

    primes = [2, 3, 5, 7, 11, 13]
    number = primes[-1]
    while len(primes) <= n:
        next_prime = next_prime_fib(number)
        if next_prime in primes:
            number = next_prime
        else:
            primes.append(next_prime)
            number = next_prime
    return number
