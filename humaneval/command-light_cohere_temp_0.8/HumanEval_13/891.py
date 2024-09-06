```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0:
        return 0
    if b == 0:
        return 0
    while a != 0 and b != 0:
        final_common_divisor = a // b
        a = a % b
        b = b % final_common_divisor
    return final_common_divisor

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
print(greatest_common_divisor(6, 20)))  # Output: 5
print(greatest_common_divisor(14, 12))  # Output: 4
```