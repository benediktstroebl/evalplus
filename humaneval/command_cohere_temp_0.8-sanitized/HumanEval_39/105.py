def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
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
    
    # First Fibonacci number that is prime
    fib_start = 5
    # Checking from fib_start to 2*fib_start, since every Fibonacci number is either prime or composite
    for fib_num in range(fib_start, 2*fib_start):
        if is_prime(fib_num):
            return fib_num
    
    # We didn't find a composite number, so the next one must be prime
    return prime_fib(n - 1)