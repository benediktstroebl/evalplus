### Greatest Common Divisor (GCD) using the Euclidean Algorithm
#### Python Script
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b
    
    Args:
        a (int): The first integer
        b (int): The second integer
    
    Returns:
        int: The greatest common divisor of a and b
    
    Examples:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """

    # Base case: If b is zero, the GCD is a
    if b == 0:
        return a
    
    # Recursive case: GCD(a, b) is the same as GCD(b, a % b)
    # The % operator gives the remainder of the division of a by b
    else:
        return greatest_common_divisor(b, a % b)


# Test the function
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Expected output: 1
    print(greatest_common_divisor(25, 15))  # Expected output: 5
```
This script uses the Euclidean algorithm to calculate the greatest common divisor of two integers. It works by recursively applying the formula `gcd(a, b) = gcd(b, a % b)`, where `%` denotes the remainder of the division of `a` by `b`.