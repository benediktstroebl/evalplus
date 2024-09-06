

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
    if n == 2:
        return 3
    if n == 3:
        return 5

    temp = 0
    i = 4

    while temp < n:
        i += 1
        a = i - 1
        b = i - 2

        c = a + b
        d = fibonacci_gcd(a, b)

        if d != 1:
            temp = temp
        else:
            temp = i

    return temp

