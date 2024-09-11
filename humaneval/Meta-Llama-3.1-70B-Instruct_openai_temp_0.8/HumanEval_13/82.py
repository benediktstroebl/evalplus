```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to efficiently compute the GCD.
    """
    while b!= 0:
        # Swap a and b, and replace b with the remainder of a divided by b
        a, b = b, a % b
    return abs(a)  # Return the absolute value of a


# Example use cases
print(greatest_common_divisor(3, 5))   # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5
print(greatest_common_divisor(48, 18)) # Output: 6
print(greatest_common_divisor(101, 103)) # Output: 1
```
This Python script defines a function `greatest_common_divisor(a, b)` that takes two integers as input and returns their greatest common divisor (GCD) using the Euclidean algorithm. The function repeatedly replaces `a` and `b` with `b` and the remainder of `a` divided by `b` until `b` becomes zero. At that point, the absolute value of `a` is the GCD of the original `a` and `b`.