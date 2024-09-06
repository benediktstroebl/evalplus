

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
    n_th = 0
    p_index = 1
    f_index = 1
    p_sum = 0
    f_sum = 1
    while n_th < n:
        p_sum = p_index + f_index
        p_index = f_index
        f_index = p_sum
        if is_prime(p_sum):
            n_th += 1
    return p_sum
