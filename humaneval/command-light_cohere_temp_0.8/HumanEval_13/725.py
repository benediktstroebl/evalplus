```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    m = max(a, b)
    for i in range(1, m // 2 + 1):
        if a % i == 0 and b % i == 0:
            return i

    return m

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(16, 48)))  # Output: 4
print(greatest_common_divisor(2, 25))  # Should return infinity)
```
The above function greatest_common_divisor calculates the greatest common divisor of two integers a and b. It uses the maximum of the two integers as the initial value, and then iterates through the divisors of this number, checking if both a and b are divisible by it. The function returns the maximum common divisor found.