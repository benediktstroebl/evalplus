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
    Generates and returns n-th Fibonacci number that is also prime
    """
    if n <= 0:
        return None
    x, y = 0, 1
    count = 0
    while True:
        count += 1
        next_num = x + y
        if is_prime(next_num) and count == n:
            return next_num
        x, y = y, next_num