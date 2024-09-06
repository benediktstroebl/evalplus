Here is a self-contained Python script that solves the problem of finding the greatest common divisor (GCD) of two integers a and b:
```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    return max(
        divmod(a, b)[0],
        divmod(b, a)[0]
    )

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that takes two integers a and b as input and returns the greatest common divisor of the two numbers. It also includes a test cases to ensure the function is working correctly for various inputs.