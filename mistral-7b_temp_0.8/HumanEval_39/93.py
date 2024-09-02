

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
    a = b = 1
    p = 2
    for i in range(1, n):
        a, b = b, a + b
        p = p + 1
        if a > 1 and b > 1:
            for i in range(2, int(a**0.5) + 1):
                if a % i == 0:
                    p = i
                    break
            if p > 1:
                for i in range(2, int(b**0.5) + 1):
                    if b % i == 0:
                        p = i
                        break
            if p > 1:
                return a
    return a

