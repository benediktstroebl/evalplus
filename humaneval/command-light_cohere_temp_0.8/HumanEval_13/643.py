```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    dirs = max(a, b)

    while d % a != 0 or d % b != 0:
        d += 1

    return d

# Example usage:
a = 3
b = 5
print(greatest_common_divisor(a, b))  # Output: 1
```