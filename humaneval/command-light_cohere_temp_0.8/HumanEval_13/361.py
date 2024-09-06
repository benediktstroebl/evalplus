```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    return max((i for i in range(1, min(a, b)) if a % i == 0 and b % i == 0))

# Unit tests
assert greatest_common_divisor(3, 5) == 1
assert greatest_common_divisor(25, 15) == 5
assert greatest_common_divisor(0, 5) == 0
assert greatest_common_divisor(-1, -2) == 1
assert greatest_common_divisor(1, 0) == 1
assert greatest_common_divisor(10, 2) == 5
assert greatest_common_divisor(30, 10) == 5
assert greatest_common_divisor(45, 20) == 15
```