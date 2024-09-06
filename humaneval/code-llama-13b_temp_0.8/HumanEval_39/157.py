

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
    if n <= 0:
        return -1
    fib_1 = 0
    fib_2 = 1
    fib_curr = 0
    prime_list = []
    while len(prime_list) < n:
        fib_curr = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fib_curr
        if is_prime(fib_curr):
            prime_list.append(fib_curr)
        if len(prime_list) == n:
            return prime_list[-1]

