```python
def sort_even(lst):
    even = [x for x in lst if x % 2 == 0]
    return even[:]

# Test cases
test_cases = [
    [1, 2, 3],
    [5, 6, 3, 4],
    [10, 11, 12],
]

for test in test_cases:
    actual = sort_even(test)
    assert actual == [3, 6, 5, 4], "Test case {} failed.".
```