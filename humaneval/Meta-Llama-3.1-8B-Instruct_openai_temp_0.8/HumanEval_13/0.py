```markdown
### Greatest Common Divisor (GCD) Calculator
#### Using Euclid's Algorithm

This script defines a function `greatest_common_divisor` to calculate the greatest common divisor (GCD) of two integers using Euclid's algorithm.

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
        # Swap values of a and b
        a, b = b, a % b
    return a

# Example usage:
print(greatest_common_divisor(3, 5))   # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5
```
This script uses the Euclidean algorithm, which repeatedly applies the division algorithm to find the remainder, until the remainder is zero. The last non-zero remainder is the GCD of the original two numbers.
```