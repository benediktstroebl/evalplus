**Greatest Common Divisor (GCD) Calculator**
```python
def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b.

    The GCD of two numbers is the largest number that divides both of the numbers without leaving a remainder.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The GCD of a and b.

    Examples:
        >>> gcd(3, 5)
        1
        >>> gcd(25, 15)
        5
    """
    while b!= 0:
        a, b = b, a % b
    return abs(a)


# Test the gcd function
if __name__ == "__main__":
    print(gcd(3, 5))  # Output: 1
    print(gcd(25, 15))  # Output: 5
```
This script uses the Euclidean algorithm to calculate the GCD of two integers. The algorithm works by repeatedly replacing `a` and `b` with `b` and the remainder of `a` divided by `b`, until `b` is zero. At that point, `a` is the GCD.