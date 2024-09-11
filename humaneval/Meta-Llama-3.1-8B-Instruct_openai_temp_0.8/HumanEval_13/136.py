### Greatest Common Divisor (GCD) Calculation
#### Using the Euclidean Algorithm

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    The Euclidean algorithm is used for efficient calculation of GCD.

    Args:
    a (int): The first integer
    b (int): The second integer

    Returns:
    int: The greatest common divisor of a and b
    """
    # Base case: if b is zero, the GCD is a
    if b == 0:
        return a
    # Recursive case: GCD(a, b) is the same as GCD(b, remainder of a divided by b)
    else:
        return greatest_common_divisor(b, a % b)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script uses the Euclidean algorithm to calculate the greatest common divisor of two integers `a` and `b`. The algorithm is based on the principle that the GCD of two numbers does not change if the larger number is replaced by its difference with the smaller number. This allows us to successively reduce the problem size until the base case is reached (when `b` becomes zero).