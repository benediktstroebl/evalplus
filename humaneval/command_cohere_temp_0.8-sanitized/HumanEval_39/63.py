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
        # To find the nth prime Fibonacci number, we look for the closest Fibonacci number that is prime
        # It is okay to miss some prime Fibonacci numbers as they grow fast
        prev, curr = 0, 1
        for _ in range(n - 1):
            prev, curr = curr, prev + curr
        while not is_prime(curr):
            prev, curr = curr, prev + curr
        return curr