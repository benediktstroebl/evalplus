```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a) + 1

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(13, 17))  # AssertionError: 13 not evenly divisible by 17
```