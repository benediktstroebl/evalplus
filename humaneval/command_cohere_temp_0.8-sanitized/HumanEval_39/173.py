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
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    # Make sure n is positive
    n = abs(n)
    # Initialize two variables for the Fibonacci sequence
    x, y = 0, 1
    count = 0
    while count < n:
        # If x is prime, we have found our number
        if is_prime(x):
            break
        # Calculate the next number in the Fibonacci sequence
        y = x + y
        x = y
        count += 1
    return x