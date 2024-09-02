

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
    f_num = [2, 1]
    for i in range(1, n+1):
        if i not in f_num:
            f_num.append(i)
            while f_num[-1] > f_num[-2]*1.2756:
                f_num.pop()
    return f_num[-1]
