### Greatest Common Divisor (GCD) Calculator
#### Using the Euclidean Algorithm

The Euclidean algorithm is an efficient method for calculating the greatest common divisor (GCD) of two integers.

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5

    :param a: First integer
    :param b: Second integer
    :return: Greatest common divisor of a and b
    """
    while b:
        a, b = b, a % b
    return abs(a)

# Example usage:
print(greatest_common_divisor(3, 5))   # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5
```

In this code:

*   We use the Euclidean algorithm, which iteratively applies the remainder operation to find the GCD.
*   The `while` loop continues until `b` becomes 0.
*   In each iteration, we update `a` and `b` using the remainder of `a` divided by `b`.
*   Once `b` is 0, we return the absolute value of `a`, which is the GCD of the original `a` and `b`.
*   The example usage demonstrates how to use the function with different inputs.