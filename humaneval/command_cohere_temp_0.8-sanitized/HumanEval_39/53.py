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
    Generates and returns the n-th Fibonacci number that is also prime
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    elif n == 3:
        return 5
    else:
        # A slightly optimized implementation of Fibonacci
        prev, curr = 0, 1
        for _ in range(4, n + 1):
            prev, curr = curr, prev + curr

        # Filter Fibonacci numbers that are prime
        fib_nums = [curr for curr in [prev, curr] if is_prime(curr)]
        if not fib_nums:
            return None
        return fib_nums[0]