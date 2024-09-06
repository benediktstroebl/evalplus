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
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # First Fibonacci number that is prime is 5
        fib = 5
        # Next few Fibonacci numbers are prime
        for _ in range(n - 2):
            if is_prime(fib):
                fib = fib * 2 + fib
                if is_prime(fib):
                    return fib
            else:
                return None
        # If we reach here, then the required number is prime and a Fibonacci number
        return fib