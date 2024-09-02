

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
    num1, num2, count = 0, 1, 0
    while count != n:
        num1, num2 = num2, num1 + num2
        if is_prime(num2):
            count += 1
    return num2

