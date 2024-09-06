

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
        Returns the n-th number of the Fibonacci sequence.
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    def is_prime(n):
        """
        Returns True if n is prime, False otherwise.
        """
        if n == 2:
            return True
        elif n == 3:
            return True
        elif n % 2 == 0:
            return False
        elif n % 3 == 0:
            return False
        else:
            for i in range(5, int(n**0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True

    def is_fib(n):
        """
        Returns True if n is the n-th Fibonacci number, False otherwise.
        """
        if n <= 1:
            return True
        elif n == 2:
            return True
        elif n == 3:
            return True
        elif fibonacci(n-1) <= n <= fibonacci(n+1):
            return False
        else:
            return True

    def is_prime_and_fib(n):
        """
        Returns True if n is a prime Fibonacci number, False otherwise.
        """
        if is_prime(n) and is_fib(n):
            return True
        else:
            return False

    return is_prime_and_fib(n)
