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
    Returns the n-th number that is both prime and a Fibonacci number.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 2
    else:
        # Calculate the next Fibonacci number that is prime by iterating from the last Fibonacci number
        prev_fib = 89
        curr_fib = 13
        count = 2
        while True:
            if is_prime(prev_fib):
                return prev_fib
            elif is_prime(curr_fib):
                return curr_fib
            prev_fib, curr_fib = curr_fib, prev_fib + curr_fib
            count += 1
            if count >= n:
                return curr_fib