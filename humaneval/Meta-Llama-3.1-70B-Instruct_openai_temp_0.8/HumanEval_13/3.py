```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the greatest common divisor.
    The Euclidean algorithm is an efficient way to compute the greatest common divisor
    of two integers, based on the principle that the greatest common divisor of two
    numbers does not change if the larger number is replaced by its difference with
    the smaller number.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.
    """
    while b!= 0:
        a, b = b, a % b
    return a


# Example use cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5

# Test cases
if greatest_common_divisor(3, 5)!= 1:
    raise AssertionError("Test case 1 failed")
if greatest_common_divisor(25, 15)!= 5:
    raise AssertionError("Test case 2 failed")
print("All test cases passed")
```