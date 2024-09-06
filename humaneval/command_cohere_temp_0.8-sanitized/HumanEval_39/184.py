def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def prime_fib(n):
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    # Start from the 3rd Fibonacci number (index 1) since the first two Fibonacci numbers are 2 and 3, both prime
    fib_index = 1
    prev_fib = 3
    curr_fib = 5
    
    for _ in range(n - 2):
        # Generate the next Fibonacci number
        prev_fib, curr_fib = curr_fib, prev_fib + curr_fib
        
        # Check if the generated Fibonacci number is prime
        if is_prime(curr_fib):
            fib_index += 1
    
    return curr_fib