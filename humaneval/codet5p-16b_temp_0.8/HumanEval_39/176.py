

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

    prev_num = 2
    cur_num = 3
    index = 3
    while index < n:
        prev_num, cur_num = cur_num, prev_num + cur_num
        index += 1
        if is_prime(cur_num):
            if index == n:
                return cur_num
