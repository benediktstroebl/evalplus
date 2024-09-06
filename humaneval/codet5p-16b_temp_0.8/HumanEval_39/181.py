

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

    i = 1
    j = 1
    while True:
        if i < n and is_prime(j):
            i += 1
            j = next_fib(j)
        elif i == n:
            return j
        else:
            i += 1
            j = next_fib(j)
            
