def prime_fib(n):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # First Fibonacci number that is prime is 5
        fib = 5
        # Use simpler (than golden ratio based) incremental method
        # for generating subsequent prime Fibonacci numbers
        fib_inc = (fib * 2 + auxiliary_fib(fib)) // 3
        return prime_fib_internal(n - 1, fib, fib_inc)
def prime_fib_internal(n, fib, fib_inc):
    if n == 0:
        return fib
    elif n == 1:
        return fib_inc
    else:
        return prime_fib_internal(n - 1, fib_inc, fib * fib_inc // 5)
def auxiliary_fib(n):
    """
    Helper function to calculate subsequent Fibonacci numbers
    """
    if n <= 1:
        return n
    else:
        return (auxiliary_fib(n - 1) * 2 + auxiliary_fib(n - 2)) // 5