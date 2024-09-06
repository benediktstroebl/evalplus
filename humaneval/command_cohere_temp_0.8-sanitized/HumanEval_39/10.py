from itertools import count, takewhile
def is_prime(n):
    """
    is_prime checks if number is prime
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    """
    if n < 2:
        return False
    for i in count(2):
        if n % i == 0:
            return False
    return True
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
        raise ValueError("n must be a positive integer.")
    # We use the formula of Fibonacci numbers to deduce that each Fibonacci number after the first two is F[n] = F[n-1] + F[n-2].
    # When we encounter a number that is prime we store it in the list primes and thereafter continue the loop.
    # When nth turn arrives we return the last prime Fibonacci number before n.
    primes = []
    fib_gen = (fibonacci_seq for fibonacci_seq in takewhile(
        lambda x: x[0] < 2e4, ((1, 1), (1, 0))
    ))
    for fib in fib_gen:
        n1, n2 = fib
        if is_prime(n1) or is_prime(n2):
            primes.append(n1)
            primes.append(n2)
        if len(primes) == n:
            return primes.pop()