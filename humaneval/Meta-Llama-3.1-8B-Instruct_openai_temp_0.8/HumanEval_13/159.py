## Greatest Common Divisor (GCD) Calculation
### Using Euclidean Algorithm

Here's a Python script that implements the Euclidean algorithm to calculate the greatest common divisor (GCD) of two integers:

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The Euclidean algorithm is used to find the GCD. It works by iteratively
    replacing (a, b) with (b, a % b) until b is zero. At this point, a is the GCD.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.
    """
    while b!= 0:
        # Swap a and b, and update b to be the remainder of a divided by b
        a, b = b, a % b

    # At this point, a is the GCD, so return it
    return abs(a)


# Example usage:
print(greatest_common_divisor(3, 5))   # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5
```

This script uses the Euclidean algorithm, which is a well-known method for calculating the GCD of two integers. It works by iteratively replacing (a, b) with (b, a % b) until b is zero. At this point, a is the GCD.