

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
    # Check that n is a Fibonacci number
    if n <= 1:
        return 2
    elif n == 2:
        return 3
    elif n == 3:
        return 5
    else:
        # Check if n is prime
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    return 0
            return 1
        else:
            return 1
