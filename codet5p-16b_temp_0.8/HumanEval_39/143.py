

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
    num1 = 2
    num2 = 3
    for i in range(3, n):
        num3 = num1 + num2
        if is_prime(num3):
            num1 = num2
            num2 = num3
            if num3 == num1 + num2:
                return num3
    return num2

