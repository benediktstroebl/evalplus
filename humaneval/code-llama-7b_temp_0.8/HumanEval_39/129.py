

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
    def is_prime(n):
        """
        is_prime returns whether a number is prime or not
        """
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False

        i = 5
        while i ** 2 <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_fib(n):
        """
        is_fib returns whether a number is Fibonacci number or not.
        """
        a, b = 0, 1
        while a <= n:
            if a == n:
                return True
            a, b = b, a + b
        return False

    def get_fib(n):
        """
        get_fib returns the n-th Fibonacci number.
        """
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    if n < 1:
        raise ValueError
    elif n == 1:
        return 2

    n -= 1
    i = 1

    while True:
        fib_num = get_fib(i)
        if is_prime(fib_num):
            n -= 1
            if n == 0:
                return fib_num
        i += 1

