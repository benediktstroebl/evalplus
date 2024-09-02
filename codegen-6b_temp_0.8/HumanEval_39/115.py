

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
    assert n > 0, "n must be positive"
    a, b = 0, 1
    count = 0
    while count < n:
        a, b = b, a + b
        count += 1
    num = a
    while not is_prime(num):
        num += 1
    return num

