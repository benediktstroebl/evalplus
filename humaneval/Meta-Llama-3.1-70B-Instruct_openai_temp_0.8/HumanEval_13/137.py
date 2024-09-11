```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to calculate the GCD.
    
    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.
    """
    while b!= 0:
        # In each iteration, replace 'a' with 'b' and 'b' with the remainder of 'a' divided by 'b'.
        a, b = b, a % b
    
    return abs(a)  # Return the absolute value of 'a', which is now the GCD.


# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that takes two integers as arguments and returns their greatest common divisor. The function uses the Euclidean algorithm to calculate the GCD. The script also includes two test cases at the end to verify that the function works correctly.