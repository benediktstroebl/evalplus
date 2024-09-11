```markdown
### Greatest Common Divisor (GCD) Calculator

This script calculates the greatest common divisor of two integers using the Euclidean algorithm.

#### Code

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The gcd of two integers a and b is the largest positive integer that divides both a and b without leaving a remainder.

    Examples:
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    # Ensure a and b are positive integers
    a = abs(a)
    b = abs(b)

    # Base case: if b is zero, the gcd is a
    while b!= 0:
        a, b = b, a % b

    return a

# Example usage
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

#### Explanation

This script uses the Euclidean algorithm to calculate the gcd of two integers. The algorithm works by iteratively replacing `a` and `b` with `b` and the remainder of `a` divided by `b` until `b` is zero, at which point `a` is the gcd.

The example usage demonstrates how to call the `greatest_common_divisor` function with different inputs and print the results.
```

This script is a simple and efficient way to calculate the greatest common divisor of two integers in Python.