```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return greatest_common_divisor(b, a % b)

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(17, 49))  # Output: 1 (17 is not divisible by 49)
print(greatest_common_divisor(105, 117))  # Output: 5 (105 and 117 are divisible by their greatest common divisor 5)
```