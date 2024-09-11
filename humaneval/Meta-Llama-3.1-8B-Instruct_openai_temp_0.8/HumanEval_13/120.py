```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The greatest common divisor (GCD) of two integers a and b is the largest number that divides both a and b without leaving a remainder.

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
        a, b = b, a % b
    return a


# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This Python script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers using the Euclidean algorithm. The function takes two integers `a` and `b` as input and returns their greatest common divisor. The script also includes test cases to verify the correctness of the function.

**Explanation of the Code**

The `greatest_common_divisor` function uses a while loop to repeatedly apply the Euclidean algorithm, which is based on the following property:

`gcd(a, b) = gcd(b, a % b)`

where `a % b` is the remainder of `a` divided by `b`. This property is used to reduce the problem of calculating the GCD of two large numbers to that of calculating the GCD of two smaller numbers.

In each iteration of the while loop, the values of `a` and `b` are updated by assigning `b` to `a` and `a % b` to `b`. This process continues until `b` becomes 0, at which point `a` is the greatest common divisor of the original `a` and `b`.

Finally, the function returns the value of `a`, which is the greatest common divisor of the input integers.