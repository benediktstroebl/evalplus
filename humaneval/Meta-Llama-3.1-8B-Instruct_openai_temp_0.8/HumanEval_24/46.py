```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Start from n-1 and go down to 1
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it as the largest divisor
            return i
    # If no divisor is found, return 1 (as 1 is a divisor of every number)
    return 1
```

This script uses a simple loop to check each number from `n-1` down to `1` to see if it is a divisor of `n`. The first number it finds that is a divisor is the largest divisor smaller than `n`, so it returns that number. If no divisor is found, it returns `1`, because every number is divisible by `1`.