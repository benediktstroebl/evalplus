```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest divisor of n smaller than n.

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
    # If no divisor is found (this should not happen), return 1
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
```

This script defines the function `largest_divisor(n)` which takes an integer `n` as input and returns the largest number that divides `n` evenly. The function iterates from `n-1` to 1 and checks each number if it's a divisor of `n`. The first divisor found is returned as the largest divisor. If no divisor is found, the function returns 1.