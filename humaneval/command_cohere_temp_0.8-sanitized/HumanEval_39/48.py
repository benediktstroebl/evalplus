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

    Args:
        n (int): The index of the desired number.

    Returns:
        int: The n-th prime Fibonacci number.
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # Start with the 3rd Fibonacci number (5) to ensure the first two are handled.
        fib_num = 5
        
        # Iterate through Fibonacci numbers until we find the n-th prime one.
        while True:
            if is_prime(fib_num):
                if n == 1:
                    return fib_num  # Exit the loop prematurely when n=1.
                elif n == 2:
                    return fib_num
                else:
                    n -= 1
            else:
                # If the number is not prime, continue to the next Fibonacci number.
                fib_num = fib_num + fib_num
            if n == 0:
                return fib_num  # Reached the desired index, return the current Fibonacci number.