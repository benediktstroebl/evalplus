```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the Euclidean algorithm to find the GCD.

    Args:
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
    return a

if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines the `greatest_common_divisor` function, which takes two integers as input and returns their greatest common divisor. It uses the Euclidean algorithm to find the GCD, which is an efficient and well-established method for this problem.

In the `if __name__ == "__main__":` block, we test the function with the examples provided in the problem statement. The output of the script should be `1` and `5`, respectively.