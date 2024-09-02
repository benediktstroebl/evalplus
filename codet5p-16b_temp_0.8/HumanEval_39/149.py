

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

    a = 1
    b = 2
    fib_list = [2, 3]
    while len(fib_list) < n:
        a, b = b, a + b
        if b % 2 == 0:
            continue
        if all(b % i!= 0 for i in range(3, int(b ** 0.5) + 1)):
            fib_list.append(b)
    return fib_list[n - 1]

