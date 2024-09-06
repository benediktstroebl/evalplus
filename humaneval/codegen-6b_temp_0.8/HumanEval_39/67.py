

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
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        prev_fib, cur_fib = 1, 1
        for _ in range(n - 1):
            prev_fib, cur_fib = cur_fib, prev_fib + cur_fib
        return cur_fib
