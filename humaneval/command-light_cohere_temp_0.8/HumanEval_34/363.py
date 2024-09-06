```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0]]

# Test cases
tests = [
    ("[5, 3, 5, 2, 3, 3, 9, 0, 123]", [0, 2, 3, 5, 9, 123]),
    ("[1, 2, 3, 4, 5, 6]", [1, 2, 3, 4, 5]),
    ("[(1, 2), (3, 4)]", [(1, 2), (3, 4)]),
    ("[(5), (3)]", [(5), (3)]),
    ("[(1), ()]", ([1])),
    ("[(5), ()", ()),
    ("[1, 2, 3, 4, 5, 6, 7]", []),
    ("[(1, 2), (3, 4, 5)]", [(1, 2), (3, 4, 5)]),
]

for case, expected in tests:
    actual = unique(case)
    print(f"Case {case}: {actual}")
    print(f"Expected: {expected}")
    assert actual == expected
```  This code defines a function `unique` which takes a list as input and returns a new list with unique elements from the input list. It uses a individual set `seen` to keep track of elements we've encountered and then uses a list comprehension to filter out any elements that are not in the set and not 0.