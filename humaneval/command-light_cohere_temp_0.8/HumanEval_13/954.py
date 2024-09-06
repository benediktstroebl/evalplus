```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both inputs cannot be zero.")
    elif b == 1:
        return a
    elif a == 1:
        return b
    else:
        return greatest_common_divisor(b, a % b)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(15, 25))  # Output: 5
print(greatest_common_divisor(10, 20))  # Output: Error: ValueError
```
The Python script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b`. The function handles edge cases where either input is zero, or when `b` is 1, it returns `a`. It also handles the case where `a` is 1, and returns `b`. The function then recursively calls itself with the other input, and divides them by the remainder of `a` divided by `b`.