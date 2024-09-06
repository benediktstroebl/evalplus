```python
def unique(l: list):
    return list(set(l))

# Test cases
test_cases = [
    [ [5, 3, 5, 2, 3, 3, 9, 0, 123], []],
    [5, 3, 5, 2, 3, 3],
    [9, 0, 123],
    [5, 5, 123, 5, 6],
]

for test_case in test_cases:
    assert unique(test_case) == [0, 2, 3, 5, 9, 123], f"failed for {test_case}"
``` 
This code defines a function `unique` which returns a list of unique elements in the input list `l`. The function uses the `set()` function and the `list` constructor to create a set of unique elements and then converts it back to a list. The test cases are defined to ensure that the `unique` function works correctly.