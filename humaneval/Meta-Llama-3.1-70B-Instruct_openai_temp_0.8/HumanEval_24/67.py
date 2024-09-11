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
    # Start from the largest possible divisor, which is n-1
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it as the largest divisor
            return i

# Example usage
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(31))  # Output: 1
```

This script defines the `largest_divisor` function, which takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function uses a simple iterative approach, starting from `n-1` and checking each number to see if it is a divisor of `n`. The first divisor found is the largest one, so the function returns it immediately.

The script also includes example usage of the `largest_divisor` function, demonstrating its behavior for different input values.