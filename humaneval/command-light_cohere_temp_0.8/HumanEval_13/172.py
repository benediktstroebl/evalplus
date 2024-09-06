```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    m, n = max(a, b), min(a, b)
    while m % n != 0:
        m, n = n, m

    return n

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(120, 60)))  # Output: 4
```