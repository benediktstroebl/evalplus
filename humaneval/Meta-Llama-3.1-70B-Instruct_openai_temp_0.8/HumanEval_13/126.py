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
    # Ensure a is greater than or equal to b to simplify the algorithm
    if b > a:
        a, b = b, a
    
    # Base case: if b is zero, a is the GCD
    if b == 0:
        return a
    
    # Recursive case: calculate the remainder of a divided by b
    # and call the function again with b and the remainder
    else:
        return greatest_common_divisor(b, a % b)


# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
print(greatest_common_divisor(48, 18))  # Expected output: 6
print(greatest_common_divisor(101, 103))  # Expected output: 1
```