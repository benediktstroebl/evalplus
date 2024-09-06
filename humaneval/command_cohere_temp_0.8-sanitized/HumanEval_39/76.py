def is_prime(n):
    """
    Checks if a number is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_fib(n):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")
    
    # Initialize the Fibonacci sequence with the first two prime numbers
    fib = [2, 3]
    while len(fib) < n:
        next_fib = fib[-1] + fib[-2]
        if is_prime(next_fib):
            fib.append(next_fib)
        else:
            # Skip non-prime Fibonacci numbers
            pass
    
    return fib[n - 1]