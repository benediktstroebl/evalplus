```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the Euclidean algorithm to find the greatest common divisor.

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
        a, b = b, a % b
    return abs(a)

# Test cases
if __name__ == "__main__":
    assert greatest_common_divisor(3, 5) == 1, "Test case 1 failed"
    assert greatest_common_divisor(25, 15) == 5, "Test case 2 failed"
    print("All test cases passed")
```