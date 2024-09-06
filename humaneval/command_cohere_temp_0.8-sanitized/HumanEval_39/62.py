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
    Generates the n-th Fibonacci number that is also prime.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    fib_nums = [0, 1]
    for i in range(3, n + 1):
        fib_nums.append(fib_nums[i - 1] + fib_nums[i - 2])
    
    # Checks the previously generated Fibonacci numbers if they are prime
    for i in range(2, n + 1):
        if is_prime(fib_nums[i]):
            return fib_nums[i]
    
    return fib_nums[n]