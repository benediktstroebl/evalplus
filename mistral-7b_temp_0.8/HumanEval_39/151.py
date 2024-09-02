

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

    """
    Fibonacci numbers: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233
    Prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47
    """

    fib_list = [0, 1]

    for i in range(0, n):
        if (fib_list[i] > 1000000):
            return -1

        fib_list.append(fib_list[i] + fib_list[i+1])
        if (is_prime(fib_list[i+1])):
            return fib_list[i+1]

