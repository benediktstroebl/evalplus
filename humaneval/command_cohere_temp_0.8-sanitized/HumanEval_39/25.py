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
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # Iterate through Fibonacci numbers and check if each number is prime
        num = 0
        prev_num = 0
        while num <= n:
            # Calculate next number
            next_num = prev_num + num
            if next_num == num:
                return None  # Exit if overflow
            prev_num = num
            num = next_num

            # Check if num is prime and subtract 1 because index is 1-based
            if is_prime(num) and num - 1 == n:
                return num
            n -= 1