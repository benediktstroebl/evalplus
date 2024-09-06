

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
    if n <= 1:
        return 2
    elif n == 2:
        return 3
    else:
        fib_num = 0
        fib_num_2 = 1
        while fib_num < n:
            fib_num = fib_num + fib_num_2
            fib_num_2 = fib_num + fib_num_2
        # checking primality
        if n % 2 == 0:
            return 0
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return 0
        return n