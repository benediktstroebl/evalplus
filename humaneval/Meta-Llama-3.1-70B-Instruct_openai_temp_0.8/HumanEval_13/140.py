```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.
    
    This function uses the Euclidean algorithm to calculate the GCD.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return abs(a)

# Example use cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(48, 18))  # Output: 6
```

This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b` using the Euclidean algorithm. The algorithm repeatedly replaces `a` and `b` with `b` and the remainder of `a` divided by `b`, until `b` is zero. The GCD is then the absolute value of `a`.

You can run this script and use the function to calculate the GCD of any two integers.