Here is a self-contained Python function that solves the problem of getting unique elements in a list:
```python
def unique(lst):
    return list(set(lst))

# Test cases
tests = [
    [
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
        ['a', 'b', 'c', 'd'],
        [5, 6, 7, 8, 9],
    ]
)

# Run the function on test cases
for case in tests:
    assert unique(case) == case[:2] + [case[-1]]  # Should get all unique elements and the last element
```
This script defines a `unique` function that returns a new list containing only the unique elements of the input list. The test cases ensure the  that the function behaves correctly with different inputs.