

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
    num1, num2 = 1, 2
    if n == 1:
        return num1
    if n == 2:
        return num2
    for i in range(3, n+1):
        num1, num2 = num2, num1 + num2
    while not isPrime(num2):
        num2 += 2
    return num2
