```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0, ]]

# Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [1, 2, 3, 4, 5, 6, 7],
    ['a', 'b', 'c', 'd', 'e'],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
]

for test_case in test_cases:
    actual = unique(test_case)
    expected = [0, 2, 3, 5, 9, 123]
    print(f"Test case {test_case}:", actual == expected)
```  The test cases will verify that the function returns the expected unique elements correctly.