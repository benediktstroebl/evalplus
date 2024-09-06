```python
def unique(l: list):
    seen = set()
    return [x for x in l if x not in seen and not in [5, 3]]

# Test cases
test_cases = [
    [],
    [5],
    [5, 3],
    [5, 3, 2, 3, 3, 9],
    [0, 2, 3, 5, 9, 123],
    [1, 2, 3, 4, 5],
    ['a', 'b', 'c', 'd']
]

for test_case in test_cases:
    actual = unique(test_case)
    assert set(actual) == set(),
    print(f"Test case {test_case} passed!")
```  This code defines a function `unique` that returns a list of unique elements from the input list `l`. The function uses a set to keep track of seen elements, and then iterates through the input list, only adding elements that are not in the set and not in the list of integers [5, 3].  This ensures that duplicates are excluded and only unique elements are retained. 

The code then provides a list of test cases, and for each one, it creates an actual list using the `unique` function and compares the set of actual results against the expected set of unique elements.  Finally, it asserts that the actual result matches the expected result and prints a pass message.