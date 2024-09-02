

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
    assert isinstance(n, int), 'n is not an integer: %s' % n

    # fib(n) = fib(n-1) + fib(n-2)
    # fib(1) = 1
    # fib(2) = 1
    # fib(3) = 2
    # fib(4) = 3
    # fib(5) = 5
    # fib(6) = 8
    # fib(7) = 13

    l = [1, 1]

    def fib(n):
        if n <= 1:
            return n
        else:
            return l[n - 1] + l[n - 2]

    def is_prime(num):
        if num <= 1:
            return False
        elif num == 2:
            return True
        else:
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True

    for i in range(2, n + 1):
        fib_ = fib(i)
        if is_prime(fib_):
            l.append(fib_)

    return l[n]

