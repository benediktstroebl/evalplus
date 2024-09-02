

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

    if n == 0:
        return 0

    def is_prime(num):
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i = i + 6
        return True

    def fib(num):
        if num < 2:
            return 0
        if num == 2:
            return 1
        if num == 3:
            return 1
        return fib(num - 1) + fib(num - 2)

    cnt = 0
    while True:
        num = fib(cnt)
        if is_prime(num):
            return num
        cnt += 1

