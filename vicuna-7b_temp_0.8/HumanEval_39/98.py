

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
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    if a % 2 == 0 and b % 2 != 0:
        return a
    while True:
        a, b = b, a + b
        if a % 2 == 0:
            continue
        if b <= (a * 1000000) % 1000000000:
            break
        if (a * a) % 2 == 0 and (b * b) % 2 == 0:
            return (a * b) % 2
        if a % 3 == 0:
            return 1
        if b % 2 == 0:
            break
        a, b = b, a + b
    
