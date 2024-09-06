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
        # Find the nth prime Fibonacci number
        fib_prev = 0
        fib_curr = 2
        for _ in range(n - 2):
            fib_next = fib_prev + fib_curr
            fib_prev, fib_curr = fib_curr, fib_next
        # The nth prime Fibonacci number is the current Fibonacci number
        # if it is prime
        if is_prime(fib_curr):
            return fib_curr
        return None