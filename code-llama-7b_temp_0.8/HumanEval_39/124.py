

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
    def _is_prime(num: int):
        """
        _is_prime is a helper function that determines if num is a prime number.
        """
        if num <= 1:
            return False
        for divider in range(2, num):
            if num % divider == 0:
                return False
        return True

    fibs = [1, 1]
    count = 2
    while count < n:
        fibs.append(fibs[-1] + fibs[-2])
        if _is_prime(fibs[-1]):
            count += 1

    return fibs[-1]
