

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
    # 2 is the first Fibonacci number and it's also prime.
    if n == 2:
        return 2
    
    # Check if the current number is a Fibonacci number
    if n in [fib(g) for fib in fibonacci_sequence for g in fib]:
        # Check if the current number is prime
        if is_prime(n):
            return n
        # Otherwise, check the next Fibonacci number
        else:
            return prime_fib(g)
    else:
        # If the number is not a Fibonacci number,
        # check if it's prime
        if is_prime(n):
            return n
        else:
            return None
