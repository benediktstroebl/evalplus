

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
    # Check if n is a Fibonacci number
    if n <= 1:
        return n
    else:
        # Check if n is prime
        if n % 2:
            return n
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i:
                return 0
        return 1