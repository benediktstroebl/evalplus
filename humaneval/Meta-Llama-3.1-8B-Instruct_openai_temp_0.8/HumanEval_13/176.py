### Greatest Common Divisor (GCD) Calculator

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The greatest common divisor (GCD) of two integers a and b is the largest positive integer that divides both a and b without leaving a remainder.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The greatest common divisor of a and b.

    Examples:
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return abs(a)


# Test cases
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers using the Euclidean algorithm. The function takes two integers `a` and `b` as input, and returns their greatest common divisor. The script also includes test cases to demonstrate the function's correctness. 

Note: The Euclidean algorithm is an efficient method for computing the greatest common divisor of two integers. It works by iteratively replacing `a` and `b` with `b` and `a mod b`, respectively, until `b` is zero. At that point, `a` is the greatest common divisor of the original `a` and `b`. The `abs` function is used to ensure that the result is always a positive integer.