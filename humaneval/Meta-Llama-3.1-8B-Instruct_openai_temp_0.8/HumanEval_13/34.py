### Greatest Common Divisor (GCD) Calculator
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    The implementation uses the Euclidean algorithm.

    :param a: First integer
    :param b: Second integer
    :return: Greatest common divisor of a and b
    """
    while b:
        a, b = b, a % b
    return abs(a)

if __name__ == "__main__":
    # Test cases
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
```
This script implements a function `greatest_common_divisor` that calculates the greatest common divisor (GCD) of two integers `a` and `b` using the Euclidean algorithm. The function takes two integers as input and returns their GCD.

The Euclidean algorithm works by repeatedly applying the following steps:

1. If `b` is zero, return `a` (since `a` is the GCD).
2. Otherwise, replace `a` with `b` and `b` with the remainder of `a` divided by `b`.

The script includes test cases to demonstrate the function's usage and correctness.

Note that the `if __name__ == "__main__":` block is used to ensure that the test cases are only executed when the script is run directly (i.e., not when it's imported as a module by another script).