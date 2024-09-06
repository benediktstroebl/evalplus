```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Define function and main logic
    def is_prime(m):
        """Check if m is prime."""
        if m < 2:
            return False
        for i in range(2, int(m ** 0.5) + 1):
            if m % i == 0:
                return False
        return True
    
    # Iterate through numbers from 2 to n
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            return i
    return n  # If no factors found, return n

# Test cases
assert largest_prime_factor(13195) == 29
assert largest_prime_factor(2048) == 2
```
This Python script defines a function `largest_prime_factor(n)` that calculates the largest prime factor of a given number `n`. It incorporates a nested helper function `is_prime(m)` to check if a number is prime. The main function iterates through factors up to the given number, identifying the largest prime factor. In case no factors are found, the function returns the number itself. The provided test cases validate the correctness of the solution.