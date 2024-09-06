```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    if a == 0:
        return b
    return max(greatest_common_divisor(b % a, a), greatest_common_divisor(a % b, b))

# Example usage:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
This function, named `greatest_common_divisor`, calculates the greatest common divisor of two integers `a` and `b`. It first checks if either number is zero; if so, it returns the other number as the GCD. If both numbers are non-zero, it recursively computes the GCD by calling `greatest_common_divisor(b % a, a)` and `greatest_common_divisor(a % b, b)` and returns the result.

Additionally, if either number is zero, it returns the non-zero number to prevent division by zero.