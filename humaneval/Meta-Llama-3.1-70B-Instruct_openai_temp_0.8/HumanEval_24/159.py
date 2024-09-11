```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest number that divides n evenly, smaller than n.

    Example:
        >>> largest_divisor(15)
        5
    """
    # Start from the number just below n, and iterate downwards.
    # The first number that divides n evenly will be the largest.
    for i in range(n-1, 0, -1):
        # Check if i divides n evenly.
        if n % i == 0:
            # If it does, return i.
            return i

# Test the function.
print(largest_divisor(15))  # Should print 5
```

This script defines the function `largest_divisor(n)` which takes an integer `n` as input, and returns the largest number that divides `n` evenly, smaller than `n`. 

The function iterates from `n-1` downwards, checking each number to see if it divides `n` evenly. The first number it finds that does this is the largest divisor of `n` smaller than `n`, so the function returns this number.

Finally, the script tests the function with the example given in the docstring.