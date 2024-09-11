### Greatest Common Divisor (GCD) of Two Integers
Here is a self-contained Python script that calculates the greatest common divisor (GCD) of two integers:

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.

    Example:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    # Base case: If both a and b are zero, return 0
    if a == 0 and b == 0:
        return 0
    
    # Base case: If b is zero, return a
    if b == 0:
        return a
    
    # Recursive case: Divide b into a and get the remainder
    # The GCD of a and b is the same as the GCD of b and the remainder
    remainder = a % b
    return greatest_common_divisor(b, remainder)


# Example usage:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script uses the Euclidean algorithm, which is a relatively efficient method for calculating the GCD of two integers. It's a recursive function, which is a function that calls itself repeatedly until it reaches the base case. In this case, the base case is when `b` is zero, at which point the function returns `a` as the GCD.