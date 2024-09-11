```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    The function uses the Euclidean algorithm to calculate the GCD.
    It recursively finds the remainder of the division of a by b, 
    until the remainder is 0. At that point, b is the GCD.

    Args:
    a (int): The first integer
    b (int): The second integer

    Returns:
    int: The greatest common divisor of a and b
    """
    # Base case: if a is 0, the GCD is b
    if a == 0:
        return b
    # Recursive case: call the function with b and the remainder of a by b
    else:
        return greatest_common_divisor(b % a, a)

# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as input and returns their greatest common divisor. It uses the Euclidean algorithm to calculate the GCD. The function includes docstrings to describe its purpose, arguments, and return value. The test cases at the end of the script demonstrate how to use the function.