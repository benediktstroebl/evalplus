

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

    fib_list = [2, 3]
    for i in range(1, n - 1):
        fib_list.append(fib_list[-1] + fib_list[-2])
    for num in fib_list:
        if prime_fib_recursive(num):
            return num

