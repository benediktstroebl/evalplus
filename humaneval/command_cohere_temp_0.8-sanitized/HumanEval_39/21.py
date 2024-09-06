from itertools import count, takewhile
def is_prime(n):
    """
    is_prime checks if number n is prime
    """
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True
def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n < 1:
        raise ValueError("n must be positive")
    
    # Generate prime Fibonacci sequence
    prime_fib_gen = (f for f in count(0, step=2) if is_prime(f))
    
    # Take n-th number from the sequence
    return takewhile(lambda x: x <= n, prime_fib_gen)[-1]