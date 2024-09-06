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
        # Find nth prime Fibonacci number
        count = 0
        fib_prev = 0
        fib_curr = 1
        while True:
            if is_prime(fib_curr):
                count += 1
                if count == n:
                    return fib_curr
                fib_prev, fib_curr = fib_curr, fib_prev + fib_curr
            else:
                fib_curr += fib_prev