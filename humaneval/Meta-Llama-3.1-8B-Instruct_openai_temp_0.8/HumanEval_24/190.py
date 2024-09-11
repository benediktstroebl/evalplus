### Largest Divisor Function
#### Finds the largest number that divides a given number evenly, smaller than the number itself.

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest number that divides n evenly, smaller than n.

    Example:
        >>> largest_divisor(15)
        5
    """
    # Iterate from n-1 down to 1 to find the largest divisor
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(12))  # Output: 6
print(largest_divisor(7))   # Output: 1
```

This script uses a simple iterative approach to find the largest divisor of a given number `n`. It iterates from `n-1` down to 1 and checks each number to see if it is a divisor of `n`. If a number is found to be a divisor, it is immediately returned as the result.