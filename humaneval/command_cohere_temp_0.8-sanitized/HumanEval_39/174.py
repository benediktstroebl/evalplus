def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    fib_nums = [0, 1]
    for i in range(2, n):
        next_num = fib_nums[i - 1] + fib_nums[i]
        fib_nums.append(next_num)

    # Starts searching from the n-th Fibonacci number
    for i in range(len(fib_nums), 0, -1):
        if is_prime(fib_nums[i]):
            return fib_nums[i]

    # If no prime is found in the latest Fibonacci numbers, returns the last computed prime Fibonacci number
    return fib_nums[-1]