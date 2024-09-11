### Largest Divisor Function
#### Python Script

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Start from n-1 and check if it's a divisor of n
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it as it's the largest one
            return i
    # If no divisor is found, return 1
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(12))  # Output: 6
print(largest_divisor(7))   # Output: 1
```

This script defines a function `largest_divisor(n)` that finds the largest number that divides `n` evenly, smaller than `n`. It starts from `n-1` and checks each number if it's a divisor of `n`. The first divisor found is returned as the largest one. If no divisor is found, the function returns 1.