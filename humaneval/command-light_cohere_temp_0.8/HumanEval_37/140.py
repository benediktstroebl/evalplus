```python
def sort_even(lst):
    """Sorts the list l such that the values at the even indices are equal to each other, while remaining values are sorted.
    This tests the Regional to the even list."""
    return lst[:] + [x for x in lst[1:]][::-1] + lst[2:]

# Test cases
tests = [
    [1, 2, 3],
    [5, 6, 3, 4],
    [1, 2, 3, 4, 5, 6]
]

for test in tests:
    assert sort_even(test) == [3, 6, 5, 4]
```
This code implements a function `sort_even` that sorts an input list such that even indices are sorted as equal, while odd indices maintain their original order. The test suite contains three test cases, and the `assert` statement checks if the `sort_even` function returns the expected result for each test case.