```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0

    # Find the GCD using the Euclidean algorithm
    while b:
        a, b = b, a % b
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b`. The function utilizes the Euclidean algorithm to find the GCD, and it returns the result.

The test cases demonstrate the function's functionality with different inputs.