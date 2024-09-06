

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
    num_fib = 2
    num_prime = 2

    while num_fib < n:
        next_fib = fib(num_fib)
        num_fib = next_fib
        if is_prime(next_fib):
            num_prime = next_fib

    return num_prime

