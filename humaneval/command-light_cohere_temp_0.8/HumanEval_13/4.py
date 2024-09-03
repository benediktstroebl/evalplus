```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    else:
        return max(a % d for d in range(1, min(a, b) + 1))

# Test cases
assert greatest_common_divisor(3, 5) == 1
assert greatest_common_divisor(25, 15) == 5
assert greatest_common_divisor(10, 5) == 5
assert greatest_common_divisor(40, 25) == 5
assert greatest_common_divisor(77, 56) == 13
```