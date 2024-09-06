

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
    assert n >= 1
    i, j, count = 2, 3, 1
    while True:
        temp = j
        j = i + j
        i = temp
        count += 1
        if is_prime(j) and count == n:
            return j
