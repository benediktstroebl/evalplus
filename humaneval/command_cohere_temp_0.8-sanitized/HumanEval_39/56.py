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
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # Start from the n-th Fibonacci number, then move forward
        # Only even numbers are composite so skip odd numbers
        for i in range(max(5, n - 1), int(3 * (n ** 0.5) + 7), 2):
            if is_prime(i):
                return i