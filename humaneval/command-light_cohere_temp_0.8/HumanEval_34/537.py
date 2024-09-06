Here's the solution:
```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0]]

# Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [1, 2, 3, 4, 5, 6, 7],
    ['a', 'bb', 'ccc'],
    [1, 2, 3, 'c', '1']
]

for test_case in test_cases:
    actual_result = unique(test_case)
    expected_result = [0, 2, 3, 5, 9, 123]
    print(f"Test {test_case}: Got {actual_result}, Expected {expected_result}")
```

This script defines a function `unique` that returns a sorted list of unique elements in the input list. It utilizes a done using a set to keep track of elements we have seen, and then the function loops through the input list, checking each element against the seen set. The output will be a list containing the elements that are not in the set, and are not zero.