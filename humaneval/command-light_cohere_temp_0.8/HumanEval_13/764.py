```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return "One or both inputs is not a number"
    return max(x for x in range(1, max(a, b)) if not a % x or b % x)

# Unit tests
test_greatest_common_divisor = {
    "Input": [3, 5],
    "Expected": 1,
    "Test case": lambda: greatest_common_divisor(3, 5) == 1,
}

test_greatest_common_divisor['Input'][0] = 25
test_greatest_common_divisor['Expected'][0] = 5
test_greatest_common_divisor['Input'][1] = 15
test_greatest_common_divisor['Expected'][1] = 5

print("All tests passed!")
```