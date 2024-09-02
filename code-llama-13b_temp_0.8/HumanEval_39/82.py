

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
    cur_fib = 0
    next_fib = 1
    for i in range(n):
        cur_fib, next_fib = next_fib, cur_fib + next_fib

    while True:
        if is_prime(cur_fib):
            return cur_fib
        else:
            cur_fib, next_fib = next_fib, cur_fib + next_fib

