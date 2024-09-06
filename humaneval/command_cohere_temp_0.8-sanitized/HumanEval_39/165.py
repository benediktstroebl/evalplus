def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_fib(n):
    if n < 1:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # Start from the 3rd Fibonacci number (2nd is 0) since previous numbers are not prime
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return a if is_prime(a) else None