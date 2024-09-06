

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
    n = n - 1
    num = 0
    while True:
        fib_num = fib(n)
        if is_prime(fib_num):
            num = fib_num
            break
        n += 1
    return num
