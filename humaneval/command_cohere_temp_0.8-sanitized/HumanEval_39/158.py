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
    Generates n-th Fibonacci number that is also prime
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3

    prev, curr = 0, 1
    for _ in range(n - 2):
        prev, curr = curr, prev + curr

    # This part handles the edge case where n == 0
    # The while loop ensures the last generated number is prime
    while True:
        next_num = prev + curr
        if is_prime(next_num):
            return next_num
        elif next_num < 2:
            break
        prev, curr = curr, prev + curr