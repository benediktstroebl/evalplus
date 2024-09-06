Here's the solution:
```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not float]

# Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [5, ],
    [10, 20, 100],
    [True, False, True]
]

for test_case in test_cases:
    actual = unique(test_case)
    assert set(actual) == set(test_case), f"Test case {test_case} failed"
```
This code defines a function called `unique` which takes a list `lst` as an argument and returns a new list containing the unique elements from the original list. It utilizes a unique elements are identified by comparing each element with the set `seen`, and only adding elements that are not present in the set. The test cases are provided to validate the function, and the output is compared against the expected results.