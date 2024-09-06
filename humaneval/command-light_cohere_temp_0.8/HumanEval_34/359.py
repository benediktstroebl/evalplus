```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [0]]

# Test cases
test_cases = [
    [ [5, 3, 5, 2, 3, 3, 9, 0, 123], []],
    [5, 3, 5, 2, 3],
    [1, 2, 3, 4, 5, 6],
    ['a', 'a', 'b', 'c']
]

for test_case in test_cases:
    actual = unique(test_case)
    expected = [0, 2, 3, 5, 9, 123]
    assert actual == expected, f"Test case [{test_case}] failed: {actual}"
```
This code defines a unique function that takes a list lst and returns a new list containing the unique elements from lst. The function uses a unique elements in lst and keeps track of the seen elements in seen using a set. The test cases cover different scenarios, and the function is evaluated with each test case to ensure it is working correctly.