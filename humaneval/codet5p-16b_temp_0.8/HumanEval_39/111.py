

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

    
    p = 1
    previous = 1
    prime = 3
    previous_prime = 1
    while p < n:
        previous, previous_prime = previous_prime, previous
        previous_prime = previous % prime
        previous = previous + previous_prime
        if previous_prime!= 0:
            prime += 2
        p += 1
    return previous

