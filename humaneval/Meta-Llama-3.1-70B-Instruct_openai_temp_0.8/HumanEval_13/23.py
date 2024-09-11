```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the greatest common divisor.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return a

# Test cases
print(greatest_common_divisor(3, 5))   # Expected output: 1
print(greatest_common_divisor(25, 15)) # Expected output: 5
print(greatest_common_divisor(48, 18)) # Expected output: 6
print(greatest_common_divisor(101, 103)) # Expected output: 1
```

The `greatest_common_divisor` function takes two integers `a` and `b` as input and returns their greatest common divisor. The function uses the Euclidean algorithm, which repeatedly applies the division algorithm to find the remainder of `a` divided by `b`, and then replaces `a` with `b` and `b` with the remainder. This process continues until `b` is zero, at which point `a` is the greatest common divisor.

The test cases provided demonstrate the function's behavior with different inputs.