Here's a self-contained Python function that solves the problem of getting unique elements from a list:

```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not None]

# Test cases
tests = [
    [list([5, 3, 5, 2, 3, 3, 9, 0, 123])], 
    [unique([5, 3, 5, 2, 3, 3, 3, 9, 0, 123])], 
    ["error"] # List not iterable
]

def test_unique(test_case):
    actual = unique(test_case[0])
    expected = test_case[1]
    assert actual == expected, "Test case failed: " + str(test_case)

for test in tests:
    test_unique(test)
```

The function unique takes a list as input and returns a new list containing only the unique elements from the original list. The set seen keeps track of elements encountered while iterating over the input list.