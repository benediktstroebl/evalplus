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
    Generates the n-th Fibonacci number that is also prime
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    # Initialize variables for the first two Fibonacci numbers
    a, b = 0, 1
    
    # Generate the next Fibonacci number if it is prime
    while not is_prime(b):
        a, b = b, a + b
    
    # Calculate the n-th Fibonacci number
    while n > 2:
        if n % 2 == 0:
            n //= 2
        else:
            break
    
    return b if n == 1 else a * b