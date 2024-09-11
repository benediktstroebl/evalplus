```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the GCD.
    The Euclidean algorithm is based on the principle that the greatest common divisor of two numbers does not change if the larger number is replaced by its difference with the smaller number.

    :param a: The first integer.
    :param b: The second integer.
    :return: The greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return a


# Test the function
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Expected output: 1
    print(greatest_common_divisor(25, 15))  # Expected output: 5
    print(greatest_common_divisor(48, 18))  # Expected output: 6
```

This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b` using the Euclidean algorithm. The function takes two integers as input, and returns their greatest common divisor.

The script also includes test cases to demonstrate the function's correctness. The `if __name__ == "__main__":` block ensures that the test cases are only executed when the script is run directly, not when it's imported as a module in another script.