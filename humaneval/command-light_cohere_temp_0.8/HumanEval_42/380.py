```python
def incr_list(lst):
    lst[:] = [1] + lst  # in-place increment
    return lst

# Test cases
test_incr_list = [
    (=[1, 2, 3], incr_list),
    (['abc', 'bcd'], incr_list),
    ([5, 3, 5, 2, 3, 3, 9, 0, 123], incr_list),
    ([], incr_list)
]

# Main execution
for testcase in test_incr_list:
    assert testcase[1] == testcase[2]
```