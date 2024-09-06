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
    # Make sure n is a positive integer
    n = abs(int(n))
    if n == 0:
        return 2  # 2 is the least prime Fibonacci number
    elif n == 1:
        return 3  # 3 is the second least prime Fibonacci number
    else:
        # Iterate through Fibonacci numbers and check for primes
        count, x, y = 0, 0, 0
        while count < n:
            x, y = y, x + y
            # Check if the current Fibonacci number is prime
            if is_prime(x):
                count += 1
        return x