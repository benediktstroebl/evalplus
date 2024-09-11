```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm, which is an efficient method for computing the GCD of two integers.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    # Ensure a and b are non-negative integers
    a = abs(a)
    b = abs(b)

    # If b is zero, the GCD is a
    if b == 0:
        return a

    # Otherwise, recursively call the function with b and the remainder of a divided by b
    else:
        return greatest_common_divisor(b, a % b)


# Test the function
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))   # Expected output: 1
    print(greatest_common_divisor(25, 15)) # Expected output: 5
```