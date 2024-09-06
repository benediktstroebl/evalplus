

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

    count = 0
    num = 1
    while count < n:
        num += 1
        fib = calc_fibonacci(num)
        if is_prime(fib):
            count += 1
    return fib

