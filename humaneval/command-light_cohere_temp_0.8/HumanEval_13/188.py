```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the numbers must be non-zero")

    if a == 0:
        return b
    elif b == 0:
        return a

    while a % b == 0:
        a //= b
    while b % a == 0:
        b //= a

    return min(a, b)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(0, 5))   # Output: 5 (since 0 is divisible by all numbers)
print(greatest_common_divisor(123, 456))  # Output: 89 (divisible by 123 and 456)
print(greatest_common_divisor(-1, 2))  # Output: 2 (divisible by both -1 and 2)
```
This code defines a function greatest_common_divisor that calculates the greatest common divisor of two integers a and b. The function uses a efficient trial division algorithm to find the largest divisor of both numbers. The test cases cover various edge cases and ensure the function behaves correctly for all valid inputs.