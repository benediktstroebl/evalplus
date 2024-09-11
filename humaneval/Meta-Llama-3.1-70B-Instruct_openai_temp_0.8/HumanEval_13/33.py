```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the Euclidean algorithm, which is an efficient method for 
    computing the greatest common divisor of two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.

    Examples:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    while b:
        a, b = b, a % b
    return a

# Test the function
print(greatest_common_divisor(3, 5))   # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5
print(greatest_common_divisor(48, 18)) # Output: 6
print(greatest_common_divisor(101, 103)) # Output: 1
```

This Python script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers using the Euclidean algorithm. The function takes two integers `a` and `b` as input, and returns their greatest common divisor. The script also includes some test cases to demonstrate the function's usage.