```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    Args:
    a (int): The first integer
    b (int): The second integer

    Returns:
    int: The greatest common divisor of a and b

    """
    while b:
        a, b = b, a % b
    return a

# Test cases
print(greatest_common_divisor(3, 5))   # Expected output: 1
print(greatest_common_divisor(25, 15)) # Expected output: 5
```

This script uses the Euclidean algorithm to calculate the greatest common divisor of two integers. The algorithm works by repeatedly replacing (a, b) with (b, a % b) until b is zero, at which point a is the greatest common divisor.