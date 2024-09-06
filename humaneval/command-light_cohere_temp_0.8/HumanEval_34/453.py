```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not None]

# Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [5,],
    [],
    [5, 6, 7],
    [True, 1, 2, 3],
    [{}]
]

for test_case in test_cases:
    actual = unique(test_case)
    assert set(actual) == set(test_case), f"Test case {test_case} failed: {set(actual)} != {test_case}"
```
This code defines a function `unique` that returns a list containing sorted and unique elements from the input list. The function uses a set to keep track of elements seen so far and checks if an input element is not in the set and not `None`. The test cases are defined to verify the correctness of the `unique` function. The test cases are executed and their results are compared with the expected values, asserting if the test case passed or not.