```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.
    
    This function uses the Euclidean algorithm to find the greatest common divisor.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return a

# Example use cases:
print(greatest_common_divisor(3, 5))   # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5
print(greatest_common_divisor(48, 18)) # Output: 6
```

This script defines a function `greatest_common_divisor` that calculates the greatest common divisor (GCD) of two integers using the Euclidean algorithm. The function continues to divide the larger number by the smaller one until the remainder is zero. The last non-zero remainder is the GCD.

The script includes example use cases to demonstrate how the function works.