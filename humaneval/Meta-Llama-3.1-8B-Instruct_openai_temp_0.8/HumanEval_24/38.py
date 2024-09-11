### Largest Divisor Function
#### Python Script
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n, smaller than n.

    Examples:
    >>> largest_divisor(15)
    5
    """
    # Start from n-1 and check each number if it's a divisor of n
    for i in range(n-1, 0, -1):
        # If n is divisible by i, return i as the largest divisor
        if n % i == 0:
            return i
    # If no divisor is found, return 1 (1 is a divisor of every number)
    return 1

print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor(n)` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function uses a loop to check each number from `n-1` down to 1 to see if it's a divisor of `n`. If a divisor is found, it's returned immediately. If no divisor is found, the function returns 1, as 1 is a divisor of every number.