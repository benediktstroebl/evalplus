```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.
    """
    # Start from the largest possible divisor, which is n-1
    for i in range(n - 1, 0, -1):
        # If n is divisible by i, then i is the largest divisor
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```