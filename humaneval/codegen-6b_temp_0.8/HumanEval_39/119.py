

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
    if n < 1:
        raise ValueError('argument must be greater than 1')
    if n == 1 or n == 2:
        return 2
    a, b = 2, 3
    fib_nums = {1: 2, 2: 3}
    while b < n:
        a, b = b, a + b
        if is_prime(b) and a % 10 == 1:
            fib_nums[b] = b
        if b%10 == 2:
            fib_nums[b] = None
    return fib_nums[n]
