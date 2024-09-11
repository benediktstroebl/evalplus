### Greatest Common Divisor
#### Using the Euclidean Algorithm

The Euclidean algorithm is a well-known method for calculating the greatest common divisor (GCD) of two integers. It works by repeatedly replacing `(a, b)` with `(b, a % b)` until `b` is `0`, at which point `a` is the GCD.

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.

    EXAMPLES:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    while b:
        a, b = b, a % b
    return abs(a)

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as input and returns their greatest common divisor. The function uses the Euclidean algorithm to calculate the GCD. The `while` loop continues until `b` is `0`, at which point `a` is the GCD. The `abs` function is used to ensure that the GCD is always positive, even if the input integers are negative.