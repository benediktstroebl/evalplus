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
    while b!= 0:
        a, b = b, a % b
    return abs(a)

# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
print(greatest_common_divisor(48, 18))  # Expected output: 6
print(greatest_common_divisor(101, 103))  # Expected output: 1
```

The provided Python script defines a function called `greatest_common_divisor` that takes two integers `a` and `b` as input and returns their greatest common divisor. The function uses the Euclidean algorithm, which is a well-known method for calculating the greatest common divisor of two numbers.

In the Euclidean algorithm, we repeatedly divide the larger number by the smaller one and take the remainder until the remainder is zero. The last non-zero remainder is the greatest common divisor.

The script also includes some test cases to demonstrate the function's correctness.