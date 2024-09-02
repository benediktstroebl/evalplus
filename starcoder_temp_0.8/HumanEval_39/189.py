

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
    prime_list = []
    fib_list = []
    fib_list.append(1)
    fib_list.append(2)
    while True:
        fib = sum(fib_list[-2:])
        fib_list.append(fib)
        if fib >= n:
            break
        if check_prime(fib):
            prime_list.append(fib)
    return prime_list[n - 1]

