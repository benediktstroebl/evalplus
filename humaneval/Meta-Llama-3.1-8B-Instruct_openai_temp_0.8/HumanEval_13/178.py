### Greatest Common Divisor (GCD) Calculator
#### Using Euclidean Algorithm
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The GCD of two integers is the largest positive integer that divides both numbers without leaving a remainder.

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
        # Replace 'a' with 'b' and 'b' with the remainder of 'a' divided by 'b'
        a, b = b, a % b
    return abs(a)


### Example Usage
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))   # Output: 1
    print(greatest_common_divisor(25, 15)) # Output: 5
```
This Python script defines a function `greatest_common_divisor` that uses the Euclidean algorithm to calculate the GCD of two integers. The algorithm works by iteratively replacing 'a' with 'b' and 'b' with the remainder of 'a' divided by 'b', until 'b' is zero. At that point, 'a' is the greatest common divisor. The `abs` function is used to ensure the result is always positive.