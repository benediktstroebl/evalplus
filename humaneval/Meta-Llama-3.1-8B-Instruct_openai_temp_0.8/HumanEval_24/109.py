```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
    n (int): The number to find the largest divisor for

    Returns:
    int: The largest number that divides n evenly, smaller than n

    Examples:
    >>> largest_divisor(15)
    5
    """
    # Start from n-1 and check each number if it's a divisor of n
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it as the largest divisor
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1 (since 17 is prime, its only divisor is 1)
```

This script uses a simple algorithm to find the largest divisor of a given number n. It starts from n-1 and checks each number if it divides n evenly. The first number it finds that is a divisor is returned as the largest divisor. This approach ensures that the returned divisor is the largest one smaller than n.