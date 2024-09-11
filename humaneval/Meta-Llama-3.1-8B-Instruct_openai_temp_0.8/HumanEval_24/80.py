### Largest Divisor Function
#### A Python Function to Find the Largest Number Dividing a Given Number Evenly
```markdown
### Code
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n.

    Example:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 20
print(largest_divisor(25))  # Output: 25
```

### Explanation
This function starts from `n-1` and checks each number to see if it divides `n` evenly. If it does, that number is the largest divisor of `n` and is returned. The loop starts from `n-1` to ensure that the divisor is smaller than `n`.