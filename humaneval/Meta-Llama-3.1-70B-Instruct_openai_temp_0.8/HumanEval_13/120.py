```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm, which is an efficient method 
    for computing the greatest common divisor of two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.
    """
    while b!= 0:
        a, b = b, a % b
    return abs(a)

# Example use cases:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor(a, b)` that takes two integers `a` and `b` as input and returns their greatest common divisor. The function uses the Euclidean algorithm to compute the greatest common divisor efficiently. The `while` loop continues until `b` becomes zero, at which point `a` is the greatest common divisor. The `abs` function is used to ensure the result is always non-negative. The script also includes example use cases to demonstrate the function's usage.