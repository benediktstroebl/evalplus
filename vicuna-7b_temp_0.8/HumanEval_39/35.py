

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
    if n <= 0:
        return 0
    
    # if n is prime
    if n == 2:
        return n
    elif n == 3:
        return n
    elif n % 2 == 0:
        return 0
    elif n % 3 == 0:
        return 0
    else:
        # recursive function call
        fib_n_minus_1 = prime_fib(n-1)
        if fib_n_minus_1 % 2 == 0:
            return 0
        fib_n_minus_2 = prime_fib(n-2)
        if fib_n_minus_2 % 2 == 0:
            return 0
        a = fib_n_minus_1 + fib_n_minus_2
        # check if a is prime
        if a > 1:
            while a % 2 == 0:
                a = a // 2
            while a % 3 == 0:
                a = a // 3
            if a > 1:
                return a
        return 0