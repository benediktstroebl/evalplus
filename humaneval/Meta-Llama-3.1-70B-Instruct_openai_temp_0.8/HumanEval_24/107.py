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
    # Start from n-1 and go down to 1
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return i
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(24))  # Output: 12
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns its largest divisor smaller than `n`. The function iterates from `n-1` down to `1`, checking each number to see if it is a divisor of `n`. As soon as it finds a divisor, it returns that divisor. If no divisor is found (which would be the case if `n` is prime), the function returns `1`, since `1` is a divisor of every number.