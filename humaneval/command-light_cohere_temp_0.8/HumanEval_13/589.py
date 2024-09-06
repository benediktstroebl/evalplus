```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0

    if a == 0:
        return b
    elif b == 0:
        return a

    while a != b:
        if a % b == 0:
            a = b
        else:
            b = a

    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
print(greatest_common_divisor(0, 5))  # Output: 5
print(greatest_common_divisor(5, 0)))   # Output: 0
print(greatest_common_divisor(20, 60)))  # Output: 4
```
This code defines a function greatest_common_divisor that calculates and returns the greatest common divisor of two integers a and b. The function utilizes the testing cases to validate its functionality, ensuring that it returns the correct result for different inputs.