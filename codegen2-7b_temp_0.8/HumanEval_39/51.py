

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
    n_1 = 2
    n_2 = 3
    if not n % 2:
        return n_1
    for i in range(3, int(n **.5) + 1):
        if i % 2 == 0:
            continue
        if not i % 3:
            return i
        n_1 += i
        n_2 += i
    
