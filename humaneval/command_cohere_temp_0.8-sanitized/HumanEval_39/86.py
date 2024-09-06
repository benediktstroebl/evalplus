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
        # Find nth Fibonacci number
        prev_fib, curr_fib = 0, 1
        for _ in range(n - 2):
            prev_fib, curr_fib = curr_fib, prev_fib + curr_fib
        # Filter out non-prime numbers
        return curr_fib if is_prime(curr_fib) else None