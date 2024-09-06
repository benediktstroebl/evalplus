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
    Generates n-th Fibonacci number that is also prime
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    # Starting point of the search
    start = 10 ** 5
    
    # Defines the step size for incrementing the search
    step = 10 ** 4
    
    # We use a while loop since we expect to rarely find the n-th prime Fibonacci index in the first iteration
    while True:
        # Index of the last found Fibonacci number that is prime
        last_prime_fib = 0
        
        # Iterate through the Fibonacci sequence to find the n-th prime Fibonacci number
        for i in range(start, int(2 * start)**2):
            # Checks if the current number is prime
            if is_prime(i):
                # If the current number is prime, check if it is a Fibonacci number
                if i == 2 * (i + 1) // (i - 1):
                    last_prime_fib = i
                    
                if n == 1:
                    return i
        
        # Adjust the starting point for the search
        start += step
        step //= 2
        
        # If the loop ends and we haven't found the n-th prime Fibonacci number, return the last found prime Fibonacci number
        if n == 1:
            return last_prime_fib
        else:
            n -= 1