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
        Fib_prev = 0
        Fib_curr = 1
        count = 0
        while count < n:
            # Check if the current Fibonacci number is prime
            if is_prime(Fib_curr):
                if count == n - 1:
                    return Fib_curr
                count += 1
            Fib_prev, Fib_curr = Fib_curr, Fib_prev + Fib_curr

        return None