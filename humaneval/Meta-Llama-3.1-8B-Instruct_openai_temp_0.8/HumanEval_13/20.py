```markdown
# Greatest Common Divisor (GCD) Calculator
=====================================================

This script calculates the greatest common divisor (GCD) of two integers.

## Code
--------

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

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

## Example Use Cases
--------------------

```python
# Test the function with some examples
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(12, 18))  # Output: 6
```

## Explanation
--------------

The `greatest_common_divisor` function uses the Euclidean algorithm to find the GCD of two integers. The algorithm works by repeatedly replacing `a` and `b` with `b` and `a % b` until `b` is zero. At this point, `a` is the GCD of the original `a` and `b`.
```