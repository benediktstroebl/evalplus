

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

    def is_prime(num: int) -> bool:
        """
        is_prime returns True if num is prime.
        """
        if num < 2:
            return False

        for i in range(2, num):
            if num % i == 0:
                return False

        return True

    # def is_prime(num: int) -> bool:
    #     """
    #     is_prime returns True if num is prime.
    #     """
    #     for i in range(2, num):
    #         if num % i == 0:
    #             return False

    #     return True

    # def is_prime(num: int) -> bool:
    #     """
    #     is_prime returns True if num is prime.
    #     """
    #     if num < 2:
    #         return False

    #     for i in range(2, num):
    #         if num % i == 0:
    #             return False

    #     return True

    # def is_
