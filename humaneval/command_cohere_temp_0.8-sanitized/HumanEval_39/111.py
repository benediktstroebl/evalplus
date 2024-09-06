def is_prime(n):
    """
    Checks if a number is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_fib(n):
    """
    Generates n-th Fibonacci number that is also prime
    """
    if n < 1:
        raise ValueError("n must be a positive integer.")

    count = 0
    fib_nums = [0, 1]
    while len(fib_nums) < n:
        next_num = fib_nums[-1] + fib_nums[-2]
        fib_nums.append(next_num)
        if is_prime(next_num):
            count += 1
    return fib_nums[n - 1] if count == n else -1