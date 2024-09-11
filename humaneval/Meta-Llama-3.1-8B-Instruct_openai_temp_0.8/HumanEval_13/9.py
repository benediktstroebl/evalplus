### Greatest Common Divisor (GCD) Calculator
#### Using the Euclidean Algorithm

Below is a Python function that calculates the greatest common divisor (GCD) of two integers using the Euclidean algorithm.

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The Euclidean algorithm is used for efficient computation.

    :param a: The first integer.
    :param b: The second integer.
    :return: The greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return a

# Test cases
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
```

This script uses a while loop to repeatedly apply the Euclidean algorithm, which states that the GCD of `a` and `b` is the same as the GCD of `b` and the remainder of `a` divided by `b`. When `b` becomes 0, `a` is the GCD.