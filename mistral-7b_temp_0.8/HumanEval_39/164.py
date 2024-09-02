

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
    if n < 2:
        return n
    prime = True
    f = 0
    f_ = 0
    f_next = 0
    while f <= n:
        f_next = f + f_
        if f_next == 2 or f_next == 3:
            f = f_next
        else:
            is_prime = True
            for i in range(2, int(f_next ** 0.5) + 1):
                if f_next % i == 0:
                    is_prime = False
                    break
            if is_prime:
                f = f_next
                if f == n:
                    return f
    return -1
