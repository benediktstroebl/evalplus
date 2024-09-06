

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
    def _is_prime(_number):
        if _number <= 1:
            return False
        if _number <= 3:
            return True

        if _number % 2 == 0 or _number % 3 == 0:
            return False

        i = 5
        while i*i <= _number:
            if _number % i == 0 or _number % (i+2) == 0:
                return False
            i += 6

        return True

    if n <= 2:
        return 1
    else:
        a, b = 1, 1
        i = 3
        while i <= n:
            a, b = b, a + b
            i += 1
        return b


    return None

