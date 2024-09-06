```python
def is_prime(n):
    """
    Check if a number is prime.

    If n is even 1 or is a prime, then return True.
    Otherwise, return False.
    """
# Example for all numbers
    """

    # This is the main loop
    for num in range(2, n + 1):
        # If n is even, it is not prime
        if num % 2 == 0:
            return False

    # If n is odd, check divisors up to the square root
    return True
```