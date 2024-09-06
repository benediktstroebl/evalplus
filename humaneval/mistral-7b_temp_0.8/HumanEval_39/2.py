

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
    # fib_list = [1, 2]
    fib_list = [2, 3]

    while True:
        fib_list.append(fib_list[-1] + fib_list[-2])
        if fib_list[-1] % 2 != 0:
            if is_prime(fib_list[-1]):
                return fib_list[-1]

        if len(fib_list) == n:
            return fib_list[-1]

