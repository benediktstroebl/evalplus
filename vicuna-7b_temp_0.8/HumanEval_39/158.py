

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
    # check if n is a Fibonacci number
    if n <= 1:
        return n
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    elif n > 3 and (n - 2) % 2 == 0:
        return 1
    else:
        # check if n is prime
        # implement your own prime number checker
        return 2
