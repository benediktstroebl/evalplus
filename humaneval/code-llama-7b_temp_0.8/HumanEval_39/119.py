

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
    n = n - 1
    fibs = [1, 1]
    i = 2
    while i <= n:
        fibs.append(fibs[-1] + fibs[-2])
        i = i + 1

    def is_prime(x):
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        return True

    while not is_prime(fibs[-1]):
        fibs.pop(-1)

    return fibs[-1]

