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
def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    # Starting point of the loop
    a, b = 0, 1
    for _ in range(n - 2):
        #calculating next Fibonacci number in the loop
        c = a + b
        a, b = b, c
    
    # Calculating last Fibonacci number outside the loop
    x = a + b
    
    # Checking if the calculated number is prime
    if is_prime(x):
        return x
    
    return None