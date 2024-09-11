Here's a Python script that uses the Euclidean algorithm to find the greatest common divisor (GCD) of two integers:

```markdown
### Greatest Common Divisor (GCD) Calculator
#### Description
This script uses the Euclidean algorithm to find the greatest common divisor (GCD) of two integers.

#### Code

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    Args:
        a (int): The first integer
        b (int): The second integer

    Returns:
        int: The greatest common divisor of a and b
    """
    while b!= 0:
        # Swap the values of a and b
        a, b = b, a % b
    return abs(a)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

#### Explanation
The `greatest_common_divisor` function uses the Euclidean algorithm to find the GCD of two integers `a` and `b`. The algorithm works by repeatedly replacing `a` with `b` and `b` with the remainder of `a` divided by `b`, until `b` is zero. At this point, `a` is the GCD of the original `a` and `b`. The `abs` function is used to ensure that the GCD is always positive, even if the input numbers have opposite signs.

Note that this implementation has a time complexity of O(log min(a, b)), making it efficient for large input numbers.