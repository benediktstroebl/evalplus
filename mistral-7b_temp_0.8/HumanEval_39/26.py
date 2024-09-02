

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
    for i in range(1, n):
        a, b = b, a + b
        if b % 2 == 0:
            continue
        if b < 4:
            continue
        if b <= 6:
            continue
        prime_count = 0
        for x in range(2, int(b ** 0.5) + 1):
            if b % x == 0:
                prime_count += 1
                break
        if prime_count == 0:
            break
    return b

