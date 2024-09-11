```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm, which is an efficient method for
    computing the greatest common divisor of two numbers.

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
    # Ensure a is greater than or equal to b
    if b > a:
        a, b = b, a

    # Base case: if b is 0, the GCD is a
    if b == 0:
        return a
    else:
        # Recursive case: GCD(a, b) = GCD(b, a % b)
        return greatest_common_divisor(b, a % b)

# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

Alternatively, you can also implement this function using a loop instead of recursion:
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm, which is an efficient method for
    computing the greatest common divisor of two numbers.

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
    # Ensure a is greater than or equal to b
    if b > a:
        a, b = b, a

    while b!= 0:
        a, b = b, a % b

    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```
Both of these functions will correctly calculate the greatest common divisor of two integers.