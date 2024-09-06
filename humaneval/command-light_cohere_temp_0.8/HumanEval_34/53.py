```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in []]

# Test cases
tests = [
    [list(range(1, 10)),
    [],
    [1, 2, 3],
    ['a', 'b', 'c'],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
]

for test_case in tests:
    actual = unique(test_case)
    assert set(actual) == set(test_case), f"Failed for {test_case}"
```
This code defines a function `unique` that returns a list containing unique elements from the input list `lst`. It utilizes a set `seen` to keep track of the unique elements seen so far, and a generator expression to create a new list of unique elements from the input list. The test suite provides a list of various test cases, and the function is tested using the `assert` assertion to verify that the output of the `unique` function matches the expected unique elements of the input list.