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
    Generates the n-th Fibonacci number that is also prime
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # Find the nth Fibonacci number
        prev_fib = 0
        curr_fib = 1
        for _ in range(n - 2):
            prev_fib, curr_fib = curr_fib, prev_fib + curr_fib
        
        # Convert it to prime if possible
        for _ in range(2, int(curr_fib**0.5) + 1):
            if curr_fib % _ == 0:
                curr_fib += _ - (curr_fib // _)
        
        # Check if the calculated number is prime
        if is_prime(curr_fib):
            return curr_fib
        else:
            return None