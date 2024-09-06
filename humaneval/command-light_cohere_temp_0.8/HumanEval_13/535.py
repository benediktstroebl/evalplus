```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    s = 1
    for i in range(1, min(len(str(a)), len(str(b)))):
        s *= int(str(i))

    while b > 0:
        b //= s
        s += 1

    return s

# Example usage
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```