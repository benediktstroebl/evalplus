

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
    # Check if n is prime
    if n > 1:
        # Check if n is divisible by any of its predecessors
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return 0
        # If n is not divisible by any of its predecessors, it must be prime
        return n
    return 0
