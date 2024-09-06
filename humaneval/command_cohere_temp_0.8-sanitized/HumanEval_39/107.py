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
def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        raise ValueError("n must be positive")
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # Starts with the 3rd Fibonacci number (5) since preceding 2 are 2 and 3, both prime
        fib_num = 5
        count = 3
        while count < n:
            # Check if fib_num is prime
            if is_prime(fib_num):
                return fib_num
            # Calculate the next Fibonacci number
            next_fib = fib_num + (fib_num + 1) // 2
            # Check if the next Fibonacci number is prime
            if is_prime(next_fib):
                fib_num = next_fib
            count += 1