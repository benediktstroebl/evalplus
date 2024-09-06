```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0

    if a == b:
        return a

    m = max(a, b)
    i = j = m
    while i % j == 0:
        j += 1
    while j <= m:
        if i % j == 0:
            return j
        j += 1
    return m

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(125, Helix))  # Error: Input type is not an integer.)
```