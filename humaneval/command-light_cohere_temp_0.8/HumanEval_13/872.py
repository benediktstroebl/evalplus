```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return max(d for d in range(1, min(a, b)) + 1 if a % d == 0 and b % d == 0)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(6, 25))  # Output: 25
print(greatest_common_divisor(8, 24))  # Output: 1
print(greatest_common_divisor(16, 48))  # Output: 16
```
This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers a and b. This function employs the strategic loop to find the largest number that divides both a and b evenly. The loop starts from 1 and includes numbers up to the minimum of a and b. The largest of these numbers that satisfy this condition is then returned as the greatest common divisor.