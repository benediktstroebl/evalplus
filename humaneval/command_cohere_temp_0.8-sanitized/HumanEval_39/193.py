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
    Returns the n-th Fibonacci number that is also prime
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    # Starting point of the search
    start = 10 ** 5
    
    # Increment by (fibonacci step ^ 2) since fibonacci steps tend to collide primes
    step = int(round(10 ** 4 / (2 * (math.log(start) / 2))))
    
    while True:
        # Calculate the current fibonacci number
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        
        # If a is prime, return it
        if is_prime(a):
            return a
        
        # Adjust search
        step *= 2
        # Adjust start based on probabilistic estimate
        start *= 1.01
        
        # Bail if we strayed too far from the original scale
        if start > 10 ** 8:
            break