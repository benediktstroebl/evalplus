

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

    def prime(number: int) -> bool:
        """
        prime checks whether number is a prime number or not
        >>> prime(14)
        False
        >>> prime(79)
        True
        >>> prime(47)
        True
        """
        if number % 2 == 0:
            return False
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True

    def fib(n: int) -> int:
        """
        fib returns n-th number of Fibonacci sequence.
        >>> fib(4)
        3
        >>> fib(8)
        21
        >>> fib(10)
        55
        """
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return a

    i = 3
    while True:
        if prime(fib(i)):
            if n == 1:
                return fib(i - 1)
            elif n == 2:
                return fib(i)
            else:
                n -= 1
        i += 1

