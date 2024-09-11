### Greatest Common Divisor (GCD) Calculation

Here is a Python script that uses the Euclidean algorithm to calculate the greatest common divisor (GCD) of two integers.

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    Example usage:
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b!= 0:
        # Swap a and b and update b as the remainder of a divided by b
        a, b = b, a % b
    return a

# Test cases
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Expected output: 1
    print(greatest_common_divisor(25, 15))  # Expected output: 5
    print(greatest_common_divisor(48, 18))  # Expected output: 6
```

In this script, the `greatest_common_divisor` function implements the Euclidean algorithm. This algorithm works by repeatedly replacing `(a, b)` with `(b, a % b)` until `b` is zero. At this point, `a` is the greatest common divisor of the original `a` and `b`. The test cases are included to verify the correctness of the implementation.