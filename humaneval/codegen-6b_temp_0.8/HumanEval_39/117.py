

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
    sofar = [2, 3]
    next_fib = sofar[-1] + sofar[-2]
    while next_fib < n:
        if is_prime(next_fib):
            sofar.append(next_fib)
        next_fib = sofar[-1] + sofar[-2]
    return sofar[-1]
