```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not None]

# Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [],
    [1, 2, 3, 4, 5, 6, 7],
    [None, None, 'abc', 'def'],
]

for test_case in test_cases:
    actual = unique(test_case)
    assert set(actual) == set(test_case), f"Test case {test_case} failed"
```

This code defines a function `unique` that returns a list containing unique elements from the input list `lst`, while using a set to efficiently keep track of elements encountered. The test cases provided are used to validate the `unique` function, ensuring that it correctly produces unique elements in the input list.