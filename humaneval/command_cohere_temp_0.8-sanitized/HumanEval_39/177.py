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

    # Initialize first two fibonacci numbers
    a, b = 0, 1
    count = 0

    while True:
        # Generate next fibonacci number
        c = a + b
        count += 1

        # Check if the generated number is prime
        if is_prime(c):
            if count == n:
                return c
        a, b = b, c