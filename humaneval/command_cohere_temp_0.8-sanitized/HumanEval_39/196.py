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
    Returns the n-th number that is both prime and a Fibonacci number.
    """
    if n < 1:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    prev_fib, curr_fib = 0, 1
    for _ in range(n - 2):
        next_fib = prev_fib + curr_fib
        prev_fib, curr_fib = curr_fib, next_fib
    
    # Handle the case where n is exceptionally large and we've reached the end of the Fibonacci sequence
    if n > 89:
        return prev_fib + curr_fib
    
    # Search for the desired number among the Fibonacci sequence
    while True:
        # Check if the next Fibonacci number is prime
        next_fib = prev_fib + curr_fib
        if is_prime(next_fib):
            return next_fib
        
        # If it's not prime, move to the next number in the sequence
        prev_fib, curr_fib = curr_fib, next_fib