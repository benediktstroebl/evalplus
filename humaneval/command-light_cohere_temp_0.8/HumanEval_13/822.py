```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    # Sort numbers
    a, b = map(int, (b, a)) - 1  # Reverse to make bigger number smaller
    while a % b == 0 or a % b == 0:
        a, b = b, a + b

    return b

# Test cases
test_cases = [
    (3, 5),
    (25, 15),
    (1024, 256),
    # Add more test cases here
]

test_suite = {}
for case in test_cases:
    assert greatest_common_divisor(case[0], case[1]) == case[2]
    test_suite[str(case)] = 1

print("All tests passed!")
```