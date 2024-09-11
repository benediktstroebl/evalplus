```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to calculate the greatest common divisor.
    
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return abs(a)

# Example usage:
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as input and returns their greatest common divisor. The function uses the Euclidean algorithm to calculate the greatest common divisor.

The script also includes example usage in the `if __name__ == "__main__":` block. This block is executed when the script is run directly (not when it's imported as a module), and it demonstrates how to use the `greatest_common_divisor` function with sample inputs.

Note that the `abs` function is used to ensure the result is always non-negative, even if the inputs are negative.