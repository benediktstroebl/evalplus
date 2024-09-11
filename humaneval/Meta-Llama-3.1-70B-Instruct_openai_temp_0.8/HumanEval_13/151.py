```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the greatest common divisor.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.
    """
    while b!= 0:
        a, b = b, a % b
    return abs(a)


# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5

# Additional test cases to ensure correctness
print(greatest_common_divisor(-3, 5))  # Output: 1
print(greatest_common_divisor(25, -15))  # Output: 5
print(greatest_common_divisor(0, 5))  # Output: 5
print(greatest_common_divisor(25, 0))  # Output: 25
```
This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` and returns their greatest common divisor. The function uses the Euclidean algorithm to find the GCD. It then includes several test cases to demonstrate the function's correctness.