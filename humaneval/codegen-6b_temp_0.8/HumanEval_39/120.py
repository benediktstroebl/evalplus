

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
    nth = [0, 1, 2]
    primes = [2, 3]

    if n == 1:
        return 2

    for i in range(2, n+1):
        nth.append(nth[i-1] + nth[i-2])

    if prime(nth[n+1]):
        primes.append(nth[n+1])
    return nth[n]
