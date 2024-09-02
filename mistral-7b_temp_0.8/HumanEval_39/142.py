

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

    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        prev_fib = 2
        cur_fib = 3
        while True:
            if is_prime(cur_fib) and cur_fib >= prev_fib:
                prev_fib = cur_fib
                cur_fib = cur_fib + prev_fib
                if cur_fib == n:
                    return cur_fib

