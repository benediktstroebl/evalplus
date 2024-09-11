```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the Euclidean algorithm to find the GCD of two numbers.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b!= 0:
        # Swap the values of a and b, and replace b with the remainder of a divided by b
        a, b = b, a % b
    return a


# Example usage:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor(a, b)` that calculates the greatest common divisor of two integers `a` and `b` using the Euclidean algorithm. The function takes two integers as input, and returns their greatest common divisor. The example usage section demonstrates how to use this function with the provided test cases.