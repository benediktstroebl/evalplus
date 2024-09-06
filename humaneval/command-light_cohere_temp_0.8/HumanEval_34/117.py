```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not == float('inf')]

# Test cases
test_cases = [
    [ [5, 3, 5, 2, 3, 3, 9, 0, 123], []],
    [5, 3, 5, 2, 3],
    [9, 0, 123, 5],
    [5, 5, 123],
    [5, 3, 5, 'x', 5, 9, 0]
]

for case in test_cases:
    actual = unique(case)
    assert set(actual) == set(case), f"Failed in test case [{actual}] = [{case}]"
```
The code implements a function unique that takes a list as input and returns a new list containing unique elements from the input. It uses a specific test case data to verify that the function works as expected.