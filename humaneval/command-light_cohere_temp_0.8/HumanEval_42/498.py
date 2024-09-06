```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(l[-1] + 1)
    return l

# Test cases
test_incr_list = [
    [1, 2, 3],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [],
    [21]
]

# Function tests
def test_func(test_case):
    assert incr_list(test_case) == test_case_expected, "Function returned unexpected result."
    return True

for test in test_incr_list:
    test_result = test_func(test)
    print("Test:", test, result:", test_result)
```