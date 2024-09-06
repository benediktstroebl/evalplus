```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

# Test cases
test_string_sequence = []
test_cases = [0, 10, 15, 20, 30, 40, 50]

for test_num in test_cases:
    actual_str = string_sequence(test_num)
    expected_str = f"0 {test_num}" * (test_num + 1)
    test_string_sequence.Assert expected_str
    The correct output for the given test case.

```