```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the greatest common divisor.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return a

# Test cases
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Expected output: 1
    print(greatest_common_divisor(25, 15))  # Expected output: 5
    print(greatest_common_divisor(48, 18))  # Expected output: 6
    print(greatest_common_divisor(101, 103))  # Expected output: 1
```

In this script, the `greatest_common_divisor` function takes two integers as input and returns their greatest common divisor. The function uses the Euclidean algorithm, which is a simple and efficient method for computing the greatest common divisor of two numbers. The algorithm works by repeatedly replacing `a` and `b` with `b` and the remainder of `a` divided by `b`, until `b` is zero. At that point, `a` is the greatest common divisor of the original `a` and `b`.

The test cases at the end of the script demonstrate the function's correctness with several examples.