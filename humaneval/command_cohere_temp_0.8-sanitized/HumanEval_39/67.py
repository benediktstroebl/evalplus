def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_fib(n):
    """
    Returns the n-th Fibonacci number that is also prime.
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        fib_num = fib_nums[n - 2] + fib_nums[n - 1]
        return fib_num if is_prime(fib_num) else prime_fib(n - 1)
fib_nums = {}