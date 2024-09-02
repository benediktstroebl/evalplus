

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

    count: int = 0
    n1: int = 0
    n2: int = 1
    n3: int = 0
    while count < n:
        n3 = n1 + n2
        if is_prime(n3) and is_fibonacci(n3):
            count += 1
            n1 = n2
            n2 = n3
            if count == n:
                return n3
    return -1

