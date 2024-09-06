

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
    def fib(x):
        """
        Calculate the n-th Fibonacci number using recursion.
        """
        if x <= 1:
            return x
        else:
            return fib(x-1) + fib(x-2)
        
    while True:
        if fib(n) % 2 == 0:
            return 0
        n += 1
