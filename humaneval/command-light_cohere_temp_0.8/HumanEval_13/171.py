```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return "Input is invalid"
    while a != 0 and b != 0:
        if a % b == 0:
            a = a // b
        else:
            b = b // a
    if a != 0:
        return a
    return "Input is still divisible"

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
print(greatest_common_divisor(7, 12)))  # Output: 4 (correct answer is 4)
print(greatest_common_divisor(60, 25)))  # Output: 5
print(greatest_common_divisor(1, 4)))  # Output: 1
print(greatest_common_divisor(56, 78)))  # Output: 1 (correct answer is 1)
```