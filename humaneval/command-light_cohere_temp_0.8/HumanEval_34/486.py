```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not None]

# Test cases
tests = [
    ["[5, 3, 5, 2, 3, 3, 9, 0, 123]", None],
    ["[5, 3, 5, 2, 3, 3, 9]", []],
    ["[5, 3, 5, 2, 3, 3, 9, 0]", [5, 3, 9]]],
    [(), []],
    ["[5, 3, 'abc']"]
]

for test_case in tests:
    actual = unique(test_case[0])
    expected = test_case[1]
    assert actual == expected
```
This Python function named unique solves the problem of returning a list of unique elements from an input list. It uses a using a set data structure to quickly filter out duplicate items. The function iterates through the simple Python list comprehension to filter out non-None elements and adds them to the result list.