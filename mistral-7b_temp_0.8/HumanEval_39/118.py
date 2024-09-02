

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
    if n == 1:
        return 2
    elif n == 2:
        return 3
    elif n == 3:
        return 5
    else:
        a = 0
        b = 1
        i = 0
        while i < n - 3:
            c = a + b
            if c > 1:
                if c > 2:
                    if c % 2 == 0:
                        continue
                for j in range(3, int(c ** 0.5) + 1, 2):
                    if c % j == 0:
                        break
                else:
                    return c
            i += 1
            a, b = b, c
        return -1

