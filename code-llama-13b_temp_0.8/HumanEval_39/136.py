

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
        raise ValueError('invalid argument')
    p_num = 1
    p_idx = 0
    f_prev = 1
    f_curr = 1
    f_idx = 2
    while p_idx < n:
        f_prev, f_curr = f_curr, f_prev + f_curr
        p_idx += 1
        if is_prime(f_curr):
            p_num = f_curr
            p_idx += 1
    return p_num

