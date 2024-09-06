

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

    prime_fib_mem = {}
    prime_fib_mem[0] = 2
    prime_fib_mem[1] = 3
    i = 2
    while True:
        i = prime_fib_mem[i - 2] + prime_fib_mem[i - 1]
        if is_prime(i):
            prime_fib_mem[i] = i
        if n == 0:
            return i
        n -= 1

