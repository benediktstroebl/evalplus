```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
```

This script defines the `largest_divisor` function, which iterates from `n-1` down to 1 and returns the first number it finds that divides `n` evenly (i.e., the remainder is 0). This is the largest divisor of `n` smaller than `n`. The script then tests the function with two examples. 

The use of a for loop allows us to do this in O(n) time complexity, which is efficient for numbers that are not too large. However, if we are working with very large numbers, we might be able to use more advanced algorithms or mathematical properties to improve performance.