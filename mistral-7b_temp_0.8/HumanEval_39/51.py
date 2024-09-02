

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
    a = 1
    b = 1
    current = 1
    while current < n:
        a, b = b, a + b
        if b % 2 == 0:
            continue
        for i in range(3, int(b**0.5) + 1, 2):
            if b % i == 0:
                break
        else:
            current += 1
    return b

