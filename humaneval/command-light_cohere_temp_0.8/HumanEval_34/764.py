```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not None]

# Test cases
tests = [
    [list([5, 3, 5, 2, 3, 3, 9, 0, 123])],
    [set([0, 2, 3, 5, 9, 123])]
]

for case, expected in tests:
    actual = unique(case)
    assert actual == expected, f"Case {case} failed"
```
This code defines a function `unique` that takes a list as input and returns a new list with unique elements from the original list. The function utilizes a approach by using a set to keep track of seen elements and then iterates through the original list, adding elements that are not in the set and not `None` to the result list.