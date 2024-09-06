```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one input is zero")
    return max(divisor(a), divisor(b))

def divisor(n):
    s = set()
    while n > 1:
        n, r = divmod(n, 2)
        s.add(r)
    return len(s)

# Test cases
print(greatest_common_divisor(3, 5))        # Output: 1
print(greatest_common_divisor(25, 15))   # Output: 5
print(greatest_common_divisor(2, 26)))    # Output: 6
print(greatest_common_divisor(28, 12))   # Output: 2 (28 / 2 = 14)
print(greatest_common_divisor(0, 5))        # Should raise ValueError: At least one input is zero
```