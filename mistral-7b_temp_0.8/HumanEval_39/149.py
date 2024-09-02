

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
    fib_num, fib_prev = 1, 0
    is_prime = True
    while fib_num < n:
        fib_prev, fib_num = fib_num, fib_prev + fib_num
        is_prime = any(fib_num % i == 0 for i in range(2, fib_num))
        if is_prime:
            return fib_num

