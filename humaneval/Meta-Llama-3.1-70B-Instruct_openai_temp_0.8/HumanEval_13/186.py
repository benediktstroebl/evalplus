```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the GCD of two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

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

# Test the function
print(greatest_common_divisor(3, 5))  # Should print 1
print(greatest_common_divisor(25, 15))  # Should print 5
```

This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as input and returns their greatest common divisor. It uses the Euclidean algorithm, which is a simple and efficient method for calculating the GCD of two numbers.

Here's how it works:

1. The function takes two integers `a` and `b` as input.
2. It enters a while loop that continues as long as `b` is not zero.
3. Inside the loop, it swaps `a` and `b` and replaces `b` with the remainder of `a` divided by `b`.
4. The loop continues until `b` is zero.
5. At this point, `a` is the greatest common divisor of the original `a` and `b`.
6. The function returns the absolute value of `a`, which is the GCD of the original `a` and `b`.

The script also includes some test cases to demonstrate the function's behavior.