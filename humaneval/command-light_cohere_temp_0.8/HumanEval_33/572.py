```python
def sort_third(lst):
    # Filter out the third items and keep them as they are
    lst[:2] += [x for x in lst[2:]
    lst[2:] = [x for x in lst[2] if x not in lst[:2]]
    return lst

# Test cases
test_cases = [
    [1, 2, 3],
    [5, 6, 3, 4, 8, 9, 2],
    [10, 11, 12]
]

test_results = [sort_third(test) for test in test_cases]

for test, result in zip(test_cases, test_results):
    assert list(test) == result
```