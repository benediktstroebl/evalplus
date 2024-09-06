

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
    def fibonacci(n):
        """
        Calculate the n-th Fibonacci number.
        >>> fibonacci(2)
        1
        >>> fibonacci(3)
        2
        >>> fibonacci(4)
        3
        >>> fibonacci(5)
        5
        """
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    def is_prime(n):
        """
        Return True if n is prime, False otherwise.
        >>> is_prime(2)
        True
        >>> is_prime(3)
        True
        >>> is_prime(5)
        True
        >>> is_prime(10)
        True
        >>> is_prime(11)
        True
        >>> is_prime(20)
        False
        >>> is_prime(21)
        False
        """
        if n <= 1:
            return True
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        elif n % 3 == 0:
            return False
        elif n > 3:
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

    def next_fibonacci(n):
        """
        Calculate the next Fibonacci number after n.
        >>> next_fibonacci(1)
        1
        >>> next_fibonacci(2)
        3
        >>> next_fibonacci(3)
        5
        >>> next_fibonacci(4)
        8
        >>> next_fibonacci(5)
        13
        """
        n = int(n)
        if n <= 0:
            return 0
        else:
            return fibonacci(n-1) + fibonacci(n)

    n = int(n)
    if is_prime(
