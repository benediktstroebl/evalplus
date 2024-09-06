

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
        return 0
    fib_list = [1, 1]
    i = 0
    while len(fib_list) < n + 1:
        i += 1
        fib_list.append(fib_list[i] + fib_list[i-1])
    return fib_list[n]
