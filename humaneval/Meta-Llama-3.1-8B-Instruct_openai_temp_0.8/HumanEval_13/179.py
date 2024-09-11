Here's a well-documented and self-contained Python script that calculates the greatest common divisor (GCD) of two integers using the Euclidean algorithm.

```markdown
## Greatest Common Divisor (GCD) Calculator
### Using the Euclidean Algorithm

#### Code
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The Euclidean algorithm is used to find the GCD.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The GCD of a and b.

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

#### Explanation

This script uses the Euclidean algorithm to find the GCD of two integers. The Euclidean algorithm works by repeatedly replacing (a, b) with (b, a % b) until b is 0. At that point, a is the GCD. The `abs` function is used to ensure the GCD is always positive, even if the inputs are negative.
```