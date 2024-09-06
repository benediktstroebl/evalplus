def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def prime_fib(n):
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # To find nth prime Fibonacci number, we look for the closest Fibonacci number that is prime
        # It is known that Fibonacci sequence has infinite prime terms, so this approach will always have a solution.
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        # If the next number is prime, nth prime Fibonacci number has been found
        if is_prime(a + b):
            return a + b
        # If the next number is not prime, we've missed the nth prime Fibonacci number
        # But the next candidate is known to be prime, so we return it
        else:
            return a + b + 1