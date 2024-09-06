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
    Generates the n-th Fibonacci number that is also prime.
    """
    # Ensure n is a positive integer
    n = abs(int(n))
    if n <= 0:
        return None

    # Initialize variables for the first two Fibonacci numbers
    a, b = 0, 1
    count = 0

    while not is_prime(a) or not is_prime(b):
        # Calculate the next Fibonacci number
        a, b = b, a + b

        # Increment count if both numbers are prime
        if is_prime(a) and is_prime(b):
            count += 1

        # If the count reaches n, return the last generated prime Fibonacci number
        if count == n:
            break

    return a