```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the GCD.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    # Ensure a is the larger number to simplify the algorithm
    if b > a:
        a, b = b, a

    # Base case: If b is zero, the GCD is a
    if b == 0:
        return a

    # Recursive case: Replace a with b and b with the remainder of a/b
    else:
        return greatest_common_divisor(b, a % b)


# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5

# Alternatively, you can use a loop instead of recursion
def greatest_common_divisor_loop(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the GCD.
    """

    # Ensure a is the larger number to simplify the algorithm
    if b > a:
        a, b = b, a

    while b!= 0:
        # Replace a with b and b with the remainder of a/b
        a, b = b, a % b

    return a

# Test the function
print(greatest_common_divisor_loop(3, 5))  # Expected output: 1
print(greatest_common_divisor_loop(25, 15))  # Expected output: 5
```