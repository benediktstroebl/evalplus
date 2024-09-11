```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm, which is a method for calculating 
    the greatest common divisor of two numbers. It repeatedly applies the division 
    algorithm, swapping the remainder with the divisor, until the remainder is 0.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.

    Examples:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """

    # Check if a and b are integers
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both a and b must be integers.")

    # If b is 0, the GCD is a
    if b == 0:
        return abs(a)
    
    # Otherwise, the GCD is the same as the GCD of b and the remainder of a divided by b
    else:
        return greatest_common_divisor(b, a % b)

# Test the function
print(greatest_common_divisor(3, 5))   # Expected output: 1
print(greatest_common_divisor(25, 15)) # Expected output: 5
```

Alternatively, you could implement this function without recursion using a while loop:

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm, which is a method for calculating 
    the greatest common divisor of two numbers. It repeatedly applies the division 
    algorithm, swapping the remainder with the divisor, until the remainder is 0.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.

    Examples:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """

    # Check if a and b are integers
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both a and b must be integers.")

    a = abs(a)
    b = abs(b)

    while b!= 0:
        a, b = b, a % b
    
    return a

# Test the function
print(greatest_common_divisor(3, 5))   # Expected output: 1
print(greatest_common_divisor(25, 15)) # Expected output: 5
```