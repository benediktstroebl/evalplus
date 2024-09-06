Here's the code that solves the problem of unique elements in a list, following the provided markdown:
```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not None]

# Test cases
test_cases = [
    [],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [1, 2, 3, 4, 5, 6, 7],
    ['a', 'b', 'c', 'd'],
    [1, 2, 3, True, 4],
    [None, 5, 6],
]

for test_case in test_cases:
    result = unique(test_case)
    print(f"Input: {test_case}")
    print(f"Expected Unique Elements: {', ' '.join(result))
    print("="end="yes")
```

This code defines a function `unique` that returns a list of unique elements in the input list. The function utilizes a set to keep track of seen elements, then filters out duplicates and non-null values from the input list.