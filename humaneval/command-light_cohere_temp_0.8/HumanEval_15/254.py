```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

# Test cases
test_string_sequence = []
test_cases = [(0,), (1,), (2,), (3,), (4, ''), (5,)]

# Loop through test cases
for test_num, expected in test_cases:
    actual = string_sequence(test_num)
    assert actual == expected, f"Test {test_num} failed"

print("All tests passed!")
```