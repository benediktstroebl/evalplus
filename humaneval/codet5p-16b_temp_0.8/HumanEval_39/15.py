

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

    prime_list = [2]
    a, b = 1, 2
    while len(prime_list) < n:
        c = a+b
        a = b
        b = c
        if is_prime(b):
            prime_list.append(b)
    return prime_list[-1]
