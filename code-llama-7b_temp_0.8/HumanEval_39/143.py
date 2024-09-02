

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

    def is_prime(x):
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        for i in range(3, int(x**0.5)+1, 2):
            if x % i == 0:
                return False
        return True

    fib_list = [1, 1]
    while True:
        if is_prime(fib_list[-1]):
            if len(fib_list) == n:
                return fib_list[-1]
            fib_list.append(fib_list[-1] + fib_list[-2])
        else:
            fib_list.append(fib_list[-1] + fib_list[-2])

