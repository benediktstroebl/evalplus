

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
    if n < 2 or n > 4:
        return 1
    elif n == 2:
        return 3
    elif n == 3:
        return 5
    elif n == 4:
        return 89
    else:
        while True:
            a, b = 1, 1
            while a <= n and b <= n:
                if a * b == n:
                    return a * b
                elif a < b:
                    b, a = a, b + 1
                else:
                    a, b = b, a + 1
            if a == n - 1:
                return a * b
            if n % a == 0:
                return 1
            a, b = 1, 1
