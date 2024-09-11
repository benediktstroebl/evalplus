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

    # Ensure a and b are positive integers
    a = abs(a)
    b = abs(b)

    # If b is zero, the GCD is a
    if b == 0:
        return a
    else:
        # Otherwise, recursively call the function with b and the remainder of a divided by b
        return greatest_common_divisor(b, a % b)


# Test the function
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Expected output: 1
    print(greatest_common_divisor(25, 15))  # Expected output: 5
    print(greatest_common_divisor(-3, 5))  # Expected output: 1
    print(greatest_common_divisor(25, -15))  # Expected output: 5
```

This script defines a recursive function `greatest_common_divisor` that calculates the greatest common divisor (GCD) of two integers `a` and `b` using the Euclidean algorithm. The function takes two integers as input and returns their GCD. The script also includes test cases to verify the function's correctness.