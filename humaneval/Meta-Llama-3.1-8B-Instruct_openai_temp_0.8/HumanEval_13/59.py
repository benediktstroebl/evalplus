### Greatest Common Divisor (GCD) Calculator
#### Using the Euclidean Algorithm

Here's a Python script that calculates the greatest common divisor (GCD) of two integers using the Euclidean algorithm:

```markdown
### Code

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """Return the greatest common divisor of two integers a and b.

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
    return abs(a)


# Example usage:
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
```

### Explanation

The Euclidean algorithm is an efficient method for calculating the greatest common divisor (GCD) of two integers. It works by iteratively replacing `a` and `b` with `b` and the remainder of `a` divided by `b` until `b` is zero. At that point, `a` is the GCD.

In this implementation, we use a simple while loop to perform the Euclidean algorithm. We also use the `abs` function to ensure that the result is always positive, even if the input integers are negative.

The example usage at the end shows how to use the `greatest_common_divisor` function to calculate the GCD of two integers.
```