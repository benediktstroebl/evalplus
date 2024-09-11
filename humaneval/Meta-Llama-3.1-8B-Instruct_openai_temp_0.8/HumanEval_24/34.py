```markdown
## Largest Divisor Function
### A Python function to find the largest divisor of a given number.

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n that is smaller than n.

    Examples:
    >>> largest_divisor(15)
    5
    """
    # Start from n-1 and check if it's a divisor of n
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it as the largest divisor
            return i

    # If no divisor is found, return 1 (1 divides every number)
    return 1

# Example usage
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(7))   # Output: 1
```

In this code, the `largest_divisor` function takes an integer `n` as input and checks all numbers from `n-1` down to 1 to find the largest divisor of `n`. It uses the modulo operator (`%`) to check if a number `i` is a divisor of `n`. The function returns the largest divisor found, or 1 if no divisor is found.