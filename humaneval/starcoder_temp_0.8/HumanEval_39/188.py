

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
    x = [1, 1]
    for i in range(2, n+1):
        x.append(x[-2] + x[-1])
        while not isprime(x[-1]):
            x[-1] += 1
    return x[n]
