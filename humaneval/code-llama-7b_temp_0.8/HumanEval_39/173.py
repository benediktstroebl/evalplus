

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
    if n == 2:
        return 3

    i = 2
    fib_list = [2, 3]
    while len(fib_list) < n:
        i += 1
        fib_num = sum(fib_list[-2:])
        fib_list.append(fib_num)

    return fib_list[-1]

