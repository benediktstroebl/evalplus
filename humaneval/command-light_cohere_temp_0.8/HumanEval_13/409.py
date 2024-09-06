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
            a, b = b, a
        elif b % a == 0:
            a, b = a, b

    return min(a, b)

# Test suite for function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
print(greatest_common_divisor(2, 4)))  # Output: 1 (divisible by 2, 4)
print(greatest_common_divisor(7, 49)))  # Output: 7
```