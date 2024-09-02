

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
    fib_list = [2, 3]
    n_fib_num = fib_list[-1] + fib_list[-2]
    while n_fib_num < n:
        if is_prime(n_fib_num):
            fib_list.append(n_fib_num)
        n_fib_num = fib_list[-1] + fib_list[-2]
    return fib_list[n-1]
