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
    # Ensure a is the larger number
    if b > a:
        a, b = b, a
    
    # Use the Euclidean algorithm to find the greatest common divisor
    while b:
        a, b = b, a % b
    
    return a

# Test cases
if __name__ == "__main__":
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(48, 18) == 6
```

This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as arguments and returns their greatest common divisor. It uses the Euclidean algorithm to calculate the greatest common divisor, which is a efficient method for computing the greatest common divisor of two integers.

The script also includes test cases to verify that the function works correctly. If the function passes all the test cases, it prints nothing, indicating that the function is working correctly.