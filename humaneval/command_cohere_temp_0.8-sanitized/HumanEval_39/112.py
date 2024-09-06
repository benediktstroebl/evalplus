def is_prime(n):
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
        prime_fib_prev = prime_fib(n - 1)
        if prime_fib_prev is None:
            return None
        prime_fib_curr = prime_fib(n - 2)
        if prime_fib_curr is None:
            return None
        return prime_fib_prev if is_prime(prime_fib_curr) else prime_fib_curr