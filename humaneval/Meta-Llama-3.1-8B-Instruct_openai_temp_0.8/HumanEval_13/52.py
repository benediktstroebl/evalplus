**Greatest Common Divisor (GCD) Calculator**
==============================================

The following Python script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers using the Euclidean algorithm.

```markdown
### Code
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    Args:
        a (int): The first integer
        b (int): The second integer

    Returns:
        int: The greatest common divisor of a and b

    Examples:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    while b!= 0:
        a, b = b, a % b
    return abs(a)

# Example usage
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

### Explanation

The `greatest_common_divisor` function uses the Euclidean algorithm to find the greatest common divisor of two integers. The algorithm works by recursively replacing 'a' with 'b' and 'b' with the remainder of 'a' divided by 'b' until 'b' is zero. At this point, 'a' is the greatest common divisor.

The `abs` function is used to ensure that the result is always positive, even if the input integers are negative.

The example usage at the end demonstrates how to use the `greatest_common_divisor` function to calculate the greatest common divisor of two integers.