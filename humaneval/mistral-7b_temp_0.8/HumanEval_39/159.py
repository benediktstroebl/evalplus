

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
    fib = 1
    fib_prev = 0
    for _ in range(n-2):
        if fib % 2 == 0:
            fib_prev, fib = fib, fib+fib_prev
        elif fib == 3:
            return fib
        else:
            for i in range(3, int(fib**0.5)+1, 2):
                if fib % i == 0:
                    fib_prev, fib = fib, fib+fib_prev
                    break
            else:
                return fib
