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
    Returns the n-th number that is both prime and a Fibonacci number.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 2
    else:
        # Calculate nth Fibonacci number
        prev_fib = 0
        curr_fib = 1
        for _ in range(2, n + 1):
            prev_fib, curr_fib = curr_fib, prev_fib + curr_fib
        
        # Filter the Fibonacci numbers that are also prime
        fib_primes = [fib for fib in [prev_fib, curr_fib] if is_prime(fib)]
        
        if not fib_primes:
            raise ValueError(f"No prime Fibonacci numbers found for n = {n}")
        elif len(fib_primes) > 1:
            return fib_primes[0]  # Return the smaller prime Fibonacci number
        else:
            return fib_primes[0]