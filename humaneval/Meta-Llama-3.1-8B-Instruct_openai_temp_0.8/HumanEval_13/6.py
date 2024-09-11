### Greatest Common Divisor (GCD) Calculation
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    The function uses the Euclidean algorithm to find the GCD.
    
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
    while b!= 0:
        a, b = b, a % b
    return abs(a)

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
This script defines a function `greatest_common_divisor` that calculates the greatest common divisor (GCD) of two integers using the Euclidean algorithm. The function uses a while loop to repeatedly replace `a` and `b` with `b` and the remainder of `a` divided by `b`, until `b` becomes zero. At that point, `a` is the GCD. The function returns the absolute value of `a` to ensure a positive result.

The script includes docstrings to explain the purpose and behavior of the function, as well as examples of its usage. It also includes test cases to demonstrate the function's correctness.