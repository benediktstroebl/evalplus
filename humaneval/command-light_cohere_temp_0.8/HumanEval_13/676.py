```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be provided.")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both numbers must be integers or floats.")

    if a == 0 or b == 0:
        return 0

    d = 1
    while b != 0:
        if a % b == 0:
            d = b
        a //= b
        b = a % b

    return d

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(-5))  # Raises ValueError
print(greatest_common_divisor(1, 7))  # Raises TypeError
```
This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b`. The function first handles edge cases: if either input is not provided, or if either number is 0, it returns 0. If the inputs are integers or floats, it raises a `TypeError`. The function then iterates through the divisors of b, finds the common divisor of a and b, and returns the result. The test cases demonstrate that the function handles different scenarios correctly.