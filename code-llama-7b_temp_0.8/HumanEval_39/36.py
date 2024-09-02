

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
    num = 1
    fib_num = 1
    while num < n:
        fib_num = fib_num + num
        if is_prime(fib_num):
            num = num + 1
        else:
            num = 1
    return fib_num

