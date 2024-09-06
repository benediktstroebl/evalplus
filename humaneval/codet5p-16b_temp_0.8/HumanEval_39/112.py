

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

    num_2 = 0
    num_1 = 1
    while True:
        num = num_1 + num_2
        if num > n:
            return num_1 + num_2
        if num == n:
            return (num_1 + num_2) // 2
        num_2 = num_1
        num_1 = num
        if num % 2 == 0:
            break

