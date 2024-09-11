```python
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        int: Greatest common divisor of a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return abs(a)

# Example usage:
print(greatest_common_divisor(3, 5))   # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5
```

**Explanation:**

This script uses the Euclidean algorithm to calculate the greatest common divisor (GCD) of two integers. The algorithm works by repeatedly replacing `a` and `b` with `b` and `a % b` until `b` is zero, at which point `a` is the GCD. The `abs` function is used to ensure the GCD is always non-negative.

**Time complexity:** O(log min(a, b))

**Space complexity:** O(1) (constant space complexity)