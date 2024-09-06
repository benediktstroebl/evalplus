

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
    # return n-th Fibonacci number that is also prime
    a, b = 0, 1
    for i in range(1, n):
        if is_prime(b):
            return b
        else:
            a, b = b, a+b

    # return 1 if there are no prime Fibonacci numbers
    return 1

