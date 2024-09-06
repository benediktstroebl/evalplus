Here is a self-contained Python script that solves the problem of returning unique elements from a list:
```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not eval('None')]

# Test cases
tests = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [[]],
    [None],
    [{'a': 1', 'b': 2'}, {'a': 1', 'b': 2}, {'a': 1', 'c': 2}],
    [0, 1, 2],
]

for test_case in tests:
    actual = unique(test_case)
    expected = test_case[1]
    print(f"Test case {i+1}: actual({actual}), expected({expected})")
    assert actual == expected, f"Failed in test case {i+1}"
```

This script defines a function unique that takes a list lst as input and returns a new list with unique elements from the original list. The set seen keeps track of elements that have already been seen, and the inner loop checks if an element is in the seen set and not `None` before adding it to the result list. The script also provides several test cases to verify the correctness of the unique function.