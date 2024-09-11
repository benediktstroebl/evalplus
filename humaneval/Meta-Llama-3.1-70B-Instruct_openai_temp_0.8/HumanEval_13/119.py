```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm, which is an efficient method for
    computing the greatest common divisor of two integers.

    :param a: The first integer.
    :param b: The second integer.
    :return: The greatest common divisor of a and b.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    # Ensure a is the larger number to simplify the algorithm
    if b > a:
        a, b = b, a

    # Base case: if b is zero, the GCD is a
    if b == 0:
        return a

    # Recursive case: call the function with b and the remainder of a divided by b
    else:
        return greatest_common_divisor(b, a % b)


# Test the function
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))   # Expected output: 1
    print(greatest_common_divisor(25, 15)) # Expected output: 5
```

This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as input and returns their greatest common divisor using the Euclidean algorithm. The function includes docstrings with usage examples and explanations.

You can save this script to a file (e.g., `gcd.py`) and run it using Python (e.g., `python gcd.py`) to test the function.