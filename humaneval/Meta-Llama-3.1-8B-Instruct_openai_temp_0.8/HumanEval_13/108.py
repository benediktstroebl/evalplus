```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the Euclidean algorithm to find the GCD of two numbers.

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
    while b!= 0:
        # Swap a and b, and replace b with the remainder of a divided by b
        a, b = b, a % b
    
    return abs(a)

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

**Explanation:**

The `greatest_common_divisor` function takes two integers `a` and `b` as input and returns their greatest common divisor (GCD).

The function uses the Euclidean algorithm to find the GCD. This algorithm repeatedly replaces `a` and `b` with `b` and the remainder of `a` divided by `b`, respectively, until `b` becomes `0`. At that point, `a` is the GCD of the original `a` and `b`.

The function includes docstrings to explain its purpose, usage, and examples. It also includes test cases to demonstrate its correctness.

**Note:** The `abs` function is used to handle negative inputs. The GCD of two negative numbers is the same as the GCD of their absolute values.