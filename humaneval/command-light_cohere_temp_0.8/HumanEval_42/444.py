```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l = [i + 1 for i in l]
    return l

# Test cases
test_incr_list = [
    (
        [1, 2, 3],
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
        [4],
    ),
]

# Function call and result comparison
for case in test_incr_list:
    actual_res = incr_list(case)
    expected_res = case
    assert actual_res == expected_res, f"Test case [{case}] failed."
```