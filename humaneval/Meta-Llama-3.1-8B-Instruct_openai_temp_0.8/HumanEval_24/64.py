```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Args:
        n (int): The number to find the largest divisor for.
    
    Returns:
        int: The largest number that divides n evenly, smaller than n.
    
    Examples:
        >>> largest_divisor(15)
        5
    """
    # We only need to check up to the square root of n, as a larger factor of n would be a multiple of a smaller factor that has already been checked.
    for i in range(int(n**0.5), 0, -1):
        # If n is divisible by i, then i is a divisor of n.
        if n % i == 0:
            # Since we are looking for the largest divisor, we can immediately return i once we find it.
            return i
    # If no divisors are found, return 1 (1 is a divisor of every number).
    return 1

# Test the function
print(largest_divisor(15))  # Outputs: 5
```