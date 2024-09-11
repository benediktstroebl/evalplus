```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    Uses the Euclidean algorithm to find the GCD.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return abs(a)


# Test the function
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
```

In this script, we define a function `greatest_common_divisor` that takes two integers `a` and `b` as input. It uses the Euclidean algorithm to find the GCD of `a` and `b`. The algorithm works by repeatedly replacing `a` and `b` with `b` and the remainder of `a` divided by `b`, until `b` is zero. The GCD is then the last non-zero value of `a`.

We then test the function with the examples provided in the docstring.