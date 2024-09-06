

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
    if n == 1 or n == 2:
        return 2
    else:
        k = 0
        p1, p2 = 2, 3
        cont = True
        while True:
            k += 1
            p3 = p1 + p2
            if is_prime(p3):
                if is_prime(p3):
                    if k == n:
                        return p3
                    else:
                        cont = False
            p1, p2 = p2, p3
            if not cont:
                break
