```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for char in string if char == substring)

# Test cases
test_suite = {}
test_suite[''] = [lambda string: how_many_times(string, 'a'), 0]
test_suite['aa'] = [lambda string: how_many_times(string, 'aa'), 3]
test_suite['aaaa'] = [lambda string: how_many_times(string, 'aaaa'), 6]

# Run the tests
for test_case, expected_output in test_suite.
```