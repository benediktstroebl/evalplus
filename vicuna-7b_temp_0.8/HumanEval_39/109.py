

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
    # function to check if n-th number is prime
    def is_prime(n: int):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    # function to check if n-th number is a Fibonacci number
    def is_fib(n: int):
        if n < 2:
            return False
        if n == 2:
            return True
        return is_fib(n - 1) or is_fib(n - 2)
    
    # function to return n-th number
    def fib(n: int):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a
    
    # check if n-th number is prime and Fibonacci
    if is_prime(n) and is_fib(n):
        # return n-th number
        return fib(n)
    else:
        # return None
        return None
