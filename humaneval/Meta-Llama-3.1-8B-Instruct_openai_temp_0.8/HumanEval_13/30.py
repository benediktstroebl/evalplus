```markdown
### Greatest Common Divisor (GCD) Calculator

#### Problem Statement

Write a Python function to find the greatest common divisor (GCD) of two integers using the Euclidean algorithm.

#### Solution

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
    while b!= 0:
        a, b = b, a % b
    return abs(a)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

#### Explanation

The `greatest_common_divisor` function uses the Euclidean algorithm to find the GCD of two integers `a` and `b`. The algorithm repeatedly applies the division algorithm, swapping the remainder with the divisor, until the remainder is zero. At this point, the non-zero remainder is the GCD.

The function takes two integers `a` and `b` as input and returns their GCD. It includes docstrings to provide documentation and examples to demonstrate its usage.

The test cases at the end of the script verify that the function works correctly for different inputs.
```