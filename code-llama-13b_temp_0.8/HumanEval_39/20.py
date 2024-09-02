

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
        raise ValueError("n should be at least 1")
    primes = [2, 3, 5, 7]
    fib_num = 0
    fib_num_plus_two = 1
    fib_num_plus_one = 1
    while True:
        fib_num = fib_num_plus_two
        fib_num_plus_two = fib_num_plus_one + fib_num_plus_two
        fib_num_plus_one = fib_num
        if is_prime(fib_num, primes):
            n -= 1
        if n == 0:
            return fib_num
