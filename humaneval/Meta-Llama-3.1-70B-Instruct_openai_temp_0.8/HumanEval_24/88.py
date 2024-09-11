```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n that is smaller than n.
    """
    # Start from n-1 and iterate downwards to find the largest divisor
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it as the largest divisor
            return i


# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(24))  # Output: 12

# Test cases:
assert largest_divisor(15) == 5
assert largest_divisor(17) == 1
assert largest_divisor(24) == 12
```