```python
def unique(lst):
    return list(set(lst))

# Test cases
unique_test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [1, 2, 3, 4, 5, 6, 7],
    ['a', 'e', 'i', 'o', 'A', 'E', 'I', 'O']
]

for test_case in unique_test_cases:
    actual_unique = unique(test_case)
    expected_unique = [0, 2, 3, 5, 9, 123]
    assert actual_unique == expected_unique, f"Test case [{test_case}] failed: {actual} != {expected}"
```
This code defines a function unique that returns a list of unique elements from an input list lst. It utilizes the class set() to remove duplicates, which is then converted to a set and converted back to a list. The function is then tested using test cases, and the output is compared to the expected unique elements.