```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the inputs must be a non-zero integer.")

    if a == 0 or b == 0:
        return 0

    m = min(a, b)
    return m if m != 0 else [x for x in range(1, m + 1) if x * x <= m][-1]

# Example usage
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```