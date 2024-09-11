```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n, smaller than n.

    >>> largest_divisor(15)
    5
    """
    # Start from n-1 and check if each number is a divisor of n
    for i in range(n - 1, 1, -1):
        # If i is a divisor of n, return it
        if n % i == 0:
            return i
    # If no divisor is found, return 1 (1 is a divisor of every number)
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(32))  # Output: 16
```

This script defines a function `largest_divisor(n)` that finds the largest number that divides `n` evenly, smaller than `n`. It uses a simple loop to check each number from `n-1` down to `2` to see if it is a divisor of `n`. If it finds a divisor, it returns that number; otherwise, it returns `1` (since `1` is a divisor of every number). The script then tests the function with several examples.