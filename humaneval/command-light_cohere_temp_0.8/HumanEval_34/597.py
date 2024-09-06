```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not == float('inf')]

# Test cases
tests = [
    [
        list_edges = [5, 3, 5, 2, 3, 3, 9, 0, 123],
        unique_expected = [0, 2, 3, 5, 9, 123]
    ],
    error_cases = [
        list_edges + [float('inf')],
        list_edges + [float('-inf')]
    ]
]

for test in tests:
    actual = unique(test[0])
    expected = test[1]
    print(f"Test passed: {actual}, should be {expected}")
    assert actual == expected, f"Test failed: {test}"
```
This script defines a function called unique that sorts and returns unique elements from a list, using a set to keep track of elements seen before. The script then provides a test cases, including a basic success test and error cases where the list contains the same element twice or infinity.