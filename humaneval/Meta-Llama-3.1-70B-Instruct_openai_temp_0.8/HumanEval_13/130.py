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
        # Swap a and b, and replace b with the remainder of a divided by b
        a, b = b, a % b
    
    # At this point, b is 0, so a is the greatest common divisor
    return abs(a)


# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

You can copy and run this script in your Python environment to test the `greatest_common_divisor` function. The script includes docstrings and comments to explain the purpose and behavior of the function, as well as test cases to verify its correctness.