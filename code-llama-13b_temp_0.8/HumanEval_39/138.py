

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

    p_num = 1
    f_num = 1
    p_count = 0

    while p_count < n:
        f_num, p_num = f_num + p_num, f_num
        if is_prime(p_num):
            p_count += 1
    return p_num

