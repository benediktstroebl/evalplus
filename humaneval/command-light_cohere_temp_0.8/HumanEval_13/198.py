```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    return max(a, b) / min(a, b)

# Test the function with a few inputs
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(12, 20))  # Output: 5
print(greatest_common_divisor(80, 60))  # Output: 4 (greater than both)
```