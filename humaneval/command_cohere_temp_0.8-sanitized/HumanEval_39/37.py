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
        fib_seq = [0, 1]
        prev_prime_idx = -1
        for idx, num in enumerate(fib_seq):
            if is_prime(num):
                prev_prime_idx = idx
        if prev_prime_idx == -1:
            return None  # No prime Fibonacci numbers found
        else:
            nth_prime_fib = fib_seq[prev_prime_idx]
            # If the nth prime Fibonacci number has been found, return it
            if idx == n - 1:
                return nth_prime_fib
            # Otherwise, keep calculating the next prime Fibonacci numbers
            else:
                next_fib = fib_seq[prev_prime_idx] + fib_seq[prev_prime_idx + 1]
                return prime_fib(n - 1) if is_prime(next_fib) else None