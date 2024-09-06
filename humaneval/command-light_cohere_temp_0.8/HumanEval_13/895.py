```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)

# Test cases
test_cases = [(3, 5), (25, 15), (1024, 256)]

for case in test_cases:
    print(f"Case {case[0]}: {case[1]} GCD: {case[1] / greatest_common_divisor(case[0], case[1])}")
```