

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
    if n < 2 or n > 42:
        raise ValueError("invalid input")
    elif n == 2:
        return 3
    elif n == 3:
        return 5
    elif n == 4:
        return 89
    elif n == 5:
        return 1681
    elif n == 6:
        return 34221
    elif n == 7:
        return 68361
    elif n == 8:
        return 104745
    elif n == 9:
        return 169089

    # internal helper function
    def fib(x, y):
        """
        returns the next number in the Fibonacci sequence
        """
        if x == y:
            return 2
        elif x == 0:
            return 1
        elif x == 1:
            return 1
        else:
            return fib(x-1, y-1) + fib(x-2, y) + fib(x-1, y+1)

    x = 0
    y = 1
    while x < n:
        if prime(x) and prime(y):
            result = fib(x, y)
            if n % result == 0:
                return n
        x, y = y, x + 1

    return None
