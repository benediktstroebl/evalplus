Here's a self-contained Python function that solves the problem of returning unique elements from a list: 

```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not None]

# Test cases
tests = [
    ( [5, 3, 5, 2, 3, 3, 9, 0, 123], "Should return list of unique elements."),
    ( [5, 3, 9, 0, 7], "Should return list of unique elements: 5, 3, 9, 0, 7"),
    (set([5, 3, 9, 0, 7]), "Should return set of unique elements: 5, 3, 9, 0, 7"),
]

for test_case, expected in tests:
    actual = unique(test_case)
    print(f"Test {test_case}: {actual}, expected: {expected}")
```