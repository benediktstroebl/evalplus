### Greatest Common Divisor (GCD) in Python

The following Python script defines a function `greatest_common_divisor` that calculates the greatest common divisor (GCD) of two integers `a` and `b` using the Euclidean algorithm.

```markdown
### Code
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

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
```

### Example Usage

```python
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script uses the Euclidean algorithm to find the GCD of two numbers. The algorithm works by repeatedly replacing `a` and `b` with `b` and the remainder of `a` divided by `b`, until `b` is zero. At that point, `a` is the GCD. This approach has a time complexity of O(log min(a, b)), making it efficient for large inputs.