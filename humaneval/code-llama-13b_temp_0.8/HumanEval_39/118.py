

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
    n1 = 1
    n2 = 1

    count = 0
    while True:
        n3 = n1 + n2
        if is_prime(n3):
            count += 1
            if count == n:
                return n3
        n1 = n2
        n2 = n3
