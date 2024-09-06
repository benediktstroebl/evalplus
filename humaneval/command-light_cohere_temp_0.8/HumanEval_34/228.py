```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not handled]

# Test cases
tests = {
    "test basic functionality": 
    [unique([5, 3, 5, 2, 3, 3, 9, 0, 123])], [0, 2, 3, 5, 9, 123]
})

# Run the tests
for case, expected in tests:
    actual = unique(case)
    assert actual == expected, f"Case: {case} failed: Expected {expected}, got {actual}"
```  This code defines a function `unique` which takes a list as input and returns a new list with unique elements from the original list. This is uses a set to keep track of elements that have been encountered, and then iterates over the original list, adding elements that are not in the set and therefore unique. 

This approach ensures that all unique elements are collected into the result list.