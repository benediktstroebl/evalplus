

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
    fibs = [1, 2]
    a = b = 2
    while True:
        a, b = b, a + b
        fibs.append(b)
        for i in range(2, int(b**0.5) + 1):
            if b % i == 0:
                break
        else:
            if prime_check(b):
                if len(fibs) - 1 >= n:
                    return fibs[n]

