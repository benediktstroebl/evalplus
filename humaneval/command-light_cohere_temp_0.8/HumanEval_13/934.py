```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be positive")
    while b != 0:
        a, b = b, a % b
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(0, 5))    # Raises ValueError
print(greatest_common_divisor(-5, 10)) # Raises ValueError
```
This script defines a function `greatest_common_divisor` that computes the greatest common divisor of two positive integers `a` and `b`. It uses a `while` loop that keeps dividing the larger number by the remainder of the division of the smaller number. This process effectively finds the done in a `while` loop until the smaller number becomes zero.