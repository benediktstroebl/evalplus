

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
    if n < 2:
        return 0
    if n < 1000:
        if n % 2 == 0:
            return 0
        if n % 3 == 0:
            return 0
        if n % 5 == 0:
            return 0
    fibonacci = (lambda a, b: a + b if a < 1000000000 else a)
    n_prime = 0
    for i in range(1, n):
        if n % i == 0:
            continue
        if fibonacci(i) > n:
            n_prime += 1
            break
    return n_prime
