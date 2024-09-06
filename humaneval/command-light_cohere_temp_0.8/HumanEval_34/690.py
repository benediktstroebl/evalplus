```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in set()]

# Test cases
tests = [
    ("[5, 3, 5, 2, 3, 3, 9, 0, 123]", "[0, 2, 3, 5, 9, 123]"),
    ("[10, 20, 30]", "[10, 20, 30]"),
    ("[1, 2, 3, 4, 5]", "[1, 2, 3, 4, 5]"),
    ("[(1, 2, 3), (4, 5)],", "[(1, 2, 3), (4, 5)]"),
    # this is empty list
    ([], []),
    # mixed types
    ([5, "hello"], [3, "world"]),
]

for test, expected in tests:
    print(unique(test), f"--- {expected}")
```

The function `unique` receives a list of elements, and returns a new list containing only the distinct elements of the original list. This is process is also creates a set of elements already appeared, and returns a new list containing only the unique elements. 

This script provides a full Python function with tests to demonstrate its functionality.