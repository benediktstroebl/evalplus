## Greatest Common Divisor (GCD) of Two Integers
### Using Euclid's Algorithm

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The function uses Euclid's algorithm, which is a step-by-step method
    for finding the greatest common divisor of two numbers.

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

    # Continue the process until b becomes zero
    while b!= 0:
        # Swap the values of a and b
        a, b = b, a % b

    # At this point, a is the greatest common divisor
    return a

# Test the function
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))   # Output: 1
    print(greatest_common_divisor(25, 15)) # Output: 5
```

This script defines a function `greatest_common_divisor` that calculates the GCD of two integers `a` and `b` using Euclid's algorithm. The algorithm repeatedly applies the following steps:

1. Divide `a` by `b` and find the remainder `r`.
2. Replace `a` with `b` and `b` with `r`.
3. Repeat steps 1 and 2 until `b` becomes zero.
4. The GCD is the last non-zero remainder, which is `a`.

The script also includes some test cases to verify the correctness of the function.