

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
    if n < 2 or n > 50:
        return -1
    elif n == 2 or n == 3:
        return 2
    elif n == 4:
        return 3
    elif n == 5:
        return 89
    elif n > 50:
        a = 1
        b = 2
        while a < n:
            if a % p == 0:
                break
            a = b
            b = b + a
        return b
    else:
        c = 0
        d = 1
        while d <= n // 2:
            if n % d == 0:
                c += d - 1
            d = d + 1
        for i in range(2, c + 1):
            if n % i == 0:
                n = n / i
                c = 0
                d = 1
                while d <= n // 2:
                    if n % d == 0:
                        c += d - 1
                    d = d + 1
                return n
        return -1
