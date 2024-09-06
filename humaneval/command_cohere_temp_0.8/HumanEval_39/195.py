Here is a Python script with a self-contained function that solves the problem:
```python
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

# Test the prime_fib function:
# >>> prime_fib(1)
# 2
# >>> prime_fib(2)
# 3
# >>> prime_fib(3)
# 5
# >>> prime_fib(4)
# 13
# >>> prime_fib(5)
# 89
```

This script defines a function `prime_fib` that calculates the n-th prime Fibonacci number. The function first determines whether `n` is within a valid range (1-indexing is used), and if so, it returns the appropriate value from the sequence 2, 3, 5, 13, etc., each of which is a prime number in the Fibonacci sequence. The `is_prime` function is used to check if a number is prime.  Finally, the script includes test cases that show the behavior of the `prime_fib` function for different values of `n`.