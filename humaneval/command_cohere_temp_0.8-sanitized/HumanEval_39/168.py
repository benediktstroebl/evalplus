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
        # Iterate through Fibonacci numbers and check if each number is prime
        count = 0
        a, b = 0, 1
        while count < n:
            x = a + b
            if is_prime(x):
                if count == n - 1:
                    return x
                count += 1
            a, b = b, a + b