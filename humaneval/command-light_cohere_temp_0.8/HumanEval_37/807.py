```python
def sort_even(lst):
    return lst[:]  # create a shallow copy

# Test cases
test_cases = [
    [ [1, 2, 3], [5, 6, 3, 4]],
    [10, 20, 30], [40, 60, 30, 20]
]

for test_case in test_cases:
    actual = sort_even(test_case)
    expected = [3, 6, 5, 4]  # from test case
    assert actual == expected, "Test case failed: " + str(test_case)
```