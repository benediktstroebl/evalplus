### Greatest Common Divisor Calculator
#### Python Script

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to calculate the GCD.

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

    # Ensure a and b are non-negative
    a = abs(a)
    b = abs(b)

    # If b is 0, the GCD is a
    while b!= 0:
        # Replace a with b and b with the remainder of a divided by b
        a, b = b, a % b

    return a


# Example usage
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
```

#### Explanation
This script defines a function `greatest_common_divisor` that calculates the greatest common divisor (GCD) of two integers `a` and `b` using the Euclidean algorithm. The function takes two integers as input and returns their GCD.

The script also includes example usage in the `if __name__ == "__main__":` block, demonstrating how to call the function with different inputs.