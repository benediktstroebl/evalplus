

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
    def fib(n: int):
        if n <= 1:
            return n
        return fib(n - 1) + fib(n - 2)

    def is_prime(n: int):
        if n in (0, 1):
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5 + 1), 2):
            if n % i == 0:
                return False
        return True

    index = 0
    while not is_prime(fib(index)):
        index += 1
    return fib(index)

