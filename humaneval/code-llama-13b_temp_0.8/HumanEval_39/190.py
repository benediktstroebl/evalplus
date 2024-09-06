

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

    a, b = 0, 1
    count = 1
    prime = []
    while True:
        temp = a
        a = b
        b = temp + b
        if is_prime(b):
            prime.append(b)
            count += 1
        if count == n:
            return b

