```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the Euclidean algorithm, which is an efficient method for computing the greatest common divisor of two integers.

    Args:
        a (int): The first integer
        b (int): The second integer

    Returns:
        int: The greatest common divisor of a and b

    Examples:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    while b!= 0:
        a, b = b, a % b
    return abs(a)

# Test cases
print(greatest_common_divisor(3, 5))   # Expected output: 1
print(greatest_common_divisor(25, 15)) # Expected output: 5
print(greatest_common_divisor(48, 18)) # Expected output: 6
```
This Python script defines a function `greatest_common_divisor(a, b)` that calculates the greatest common divisor (GCD) of two integers `a` and `b` using the Euclidean algorithm. The GCD is the largest number that divides both `a` and `b` without leaving a remainder.

The function takes two integers `a` and `b` as input and returns their GCD. It uses a while loop to repeatedly apply the Euclidean algorithm until `b` becomes zero. At that point, the GCD is the absolute value of `a`.

The script includes test cases to verify the correctness of the `greatest_common_divisor` function.