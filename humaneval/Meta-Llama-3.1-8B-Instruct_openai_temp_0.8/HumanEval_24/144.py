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
    # Start checking from the second last number (n-1) down to 1
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it as it is the largest one
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

This script uses a simple loop starting from `n - 1` down to `1` to check each number if it's a divisor of `n`. If a divisor is found, it's immediately returned as it's the largest one. If no divisor is found, the function will not return any value (in a real-world application, you should add error handling).