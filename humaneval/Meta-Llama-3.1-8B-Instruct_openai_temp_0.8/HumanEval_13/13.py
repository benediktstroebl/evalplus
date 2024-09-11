### Greatest Common Divisor (GCD) Calculator
#### Using the Euclidean Algorithm

Below is a Python script that solves the problem by implementing the Euclidean algorithm to calculate the greatest common divisor (GCD) of two integers.

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The Euclidean algorithm is used to calculate the GCD.

    Args:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The greatest common divisor of a and b.
    """

    # Base case: If b is zero, the GCD is a
    if b == 0:
        return a

    # Recursive case: Replace (a, b) with (b, a % b)
    # until b is zero
    else:
        return greatest_common_divisor(b, a % b)


# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
print(greatest_common_divisor(48, 18))  # Expected output: 6
```

This script uses the Euclidean algorithm to recursively calculate the GCD of two integers. The algorithm works by repeatedly replacing `(a, b)` with `(b, a % b)` until `b` is zero, at which point `a` is the GCD. The base case is when `b` is zero, in which case the GCD is `a`.