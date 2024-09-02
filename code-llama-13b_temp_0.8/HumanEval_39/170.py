

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
    p_count, f_count = 1, 0
    f_1 = 0
    f_2 = 1
    f_n = 0
    while (f_count < n):
        f_n = f_1 + f_2
        f_1 = f_2
        f_2 = f_n
        prime = check_prime(f_n)
        if (prime == True):
            p_count += 1
        if (prime == True and p_count == n):
            return f_n
        f_count += 1
    return -1
