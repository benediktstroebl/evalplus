```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the Euclidean algorithm to find the GCD.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return abs(a)

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as input, and returns their greatest common divisor. The function uses the Euclidean algorithm to find the GCD. The Euclidean algorithm is a method for finding the greatest common divisor of two numbers based on the principle that the greatest common divisor of two numbers does not change if the larger number is replaced by its difference with the smaller number. The function also includes a test to ensure the result is always positive.

The script then tests the function with the examples provided, and prints the results.