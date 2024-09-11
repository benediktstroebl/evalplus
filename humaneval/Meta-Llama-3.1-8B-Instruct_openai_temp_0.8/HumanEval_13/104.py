```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    Args:
        a (int): The first integer
        b (int): The second integer

    Returns:
        int: The greatest common divisor of a and b

    Examples:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    while b:
        a, b = b, a % b
    return abs(a)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script uses the Euclidean algorithm to find the greatest common divisor (GCD) of two integers. The GCD is the largest positive integer that divides both numbers without leaving a remainder.

Here's an explanation of the code:

1. The `while` loop continues until `b` is 0.
2. Inside the loop, the values of `a` and `b` are swapped and the remainder of `a` divided by `b` is calculated using the modulo operator (`%`).
3. When `b` is 0, the loop exits and the value of `a` is returned as the GCD.
4. The `abs` function is used to ensure the GCD is positive, even if the input numbers are negative.