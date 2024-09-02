

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
    if n < 1:
        return 2

    def is_prime(num: int) -> bool:
        # prime numbers are greater than 1
        if num < 2:
            return False
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True

    def fib(n1: int, n2: int) -> int:
        return n1 + n2

    current = 0
    previous = 1
    counter = 0
    while counter < n:
        current = fib(previous, current)
        if is_prime(current):
            counter += 1
        previous = current

    return current

