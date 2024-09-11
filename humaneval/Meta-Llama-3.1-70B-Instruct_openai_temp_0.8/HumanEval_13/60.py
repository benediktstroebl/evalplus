```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to calculate the GCD.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return a

# Example usage:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b` using the Euclidean algorithm. The function takes two integers as input, and returns their greatest common divisor. The `while` loop is used to repeatedly replace `a` and `b` with `b` and `a % b` until `b` is zero, at which point `a` is the GCD.

The example usage at the end of the script demonstrates how to use the `greatest_common_divisor` function with two pairs of numbers, and prints the results to the console.