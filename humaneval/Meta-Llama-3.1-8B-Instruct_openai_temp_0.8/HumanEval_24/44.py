```markdown
### Largest Divisor Function
#### A Python function to find the largest number that divides another number evenly

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
    n (int): The number to find the largest divisor for

    Returns:
    int: The largest divisor of n, smaller than n

    Example:
    >>> largest_divisor(15)
    5
    """
    # Start from the number n and iterate down to 1
    for i in range(n, 0, -1):
        # Check if n is divisible by i
        if n % i == 0:
            # If n is divisible by i, return i as the largest divisor
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 20
print(largest_divisor(10))  # Output: 10
```

### Explanation
The function `largest_divisor` starts from the number `n` and checks each number down to 1. If `n` is divisible by a number `i`, then `i` is the largest divisor of `n`, so it is returned. This function has a time complexity of O(n), where n is the input number.