```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    
    This function uses the Euclidean algorithm to find the greatest common divisor.

    Args:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The greatest common divisor of a and b.
    """
    while b!= 0:
        # Swap a and b, and replace b with the remainder of a divided by b
        a, b = b, a % b
    return abs(a)

# Test cases
print(greatest_common_divisor(3, 5))   # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5
print(greatest_common_divisor(48, 18)) # Output: 6
```

This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as input, and returns their greatest common divisor. The function uses the Euclidean algorithm, which is an efficient method for computing the greatest common divisor of two numbers. The algorithm works by repeatedly applying the division algorithm, swapping the remainder with the divisor, until the remainder is zero. The last non-zero remainder is the greatest common divisor.

The script also includes some test cases to demonstrate the function's usage.