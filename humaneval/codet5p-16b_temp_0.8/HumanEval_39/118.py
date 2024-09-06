

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

    
    def fib_prime_helper(p: int):
        f_1 = f_2 = 1
        while f_1 + f_2 < p:
            f_2 += f_1
            f_1 += f_2
        if f_1 + f_2 == p:
            return True
        return False
        
    f_1 = 1
    f_2 = 1
    while True:
        if f_1 == 1 or f_1 == 0 or f_2 == 1:
            f_1 += 1
            f_2 += 1
        elif f_1 + f_2 < n:
            f_2 += f_1
            f_1 += f_2
        elif f_1 + f_2 == n:
            if fib_prime_helper(f_1 + f_2):
                return f_1 + f_2
            else:
                f_1 += 1
                f_2 += 1

