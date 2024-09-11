```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    Example:
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
print(largest_divisor(15))  # Should print 5
```

This script defines the `largest_divisor` function as requested, which takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It works by iterating over numbers from `n-1` down to `1`, checking if each number is a divisor of `n` by using the modulo operator (`n % i == 0`). As soon as it finds a divisor, it returns that number.

You can run this script to see the output of the `largest_divisor` function for the example input `15`.