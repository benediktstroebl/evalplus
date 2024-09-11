### Greatest Common Divisor (GCD) Function
#### Using the Euclidean Algorithm

Here's a Python function that calculates the greatest common divisor (GCD) of two integers using the Euclidean algorithm.

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The Euclidean algorithm is used to find the GCD.

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
        # Swap a and b, and replace b with the remainder of a divided by b
        a, b = b, a % b
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This function uses a while loop to repeatedly apply the Euclidean algorithm, swapping the values of `a` and `b` and replacing `b` with the remainder of `a` divided by `b`, until `b` is 0. At that point, `a` is the greatest common divisor of the original `a` and `b`.