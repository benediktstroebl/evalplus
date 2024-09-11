```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to calculate the GCD.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Ensure a is the larger number to simplify the algorithm
    if b > a:
        a, b = b, a

    # Calculate the remainder of a divided by b
    while b!= 0:
        remainder = a % b
        a, b = b, remainder

    # The GCD is the last non-zero remainder
    return a

# Test cases
print(greatest_common_divisor(3, 5))   # Expected output: 1
print(greatest_common_divisor(25, 15)) # Expected output: 5
print(greatest_common_divisor(48, 18)) # Expected output: 6
print(greatest_common_divisor(101, 103)) # Expected output: 1
```