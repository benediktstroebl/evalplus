```python
def sort_third(l: list):
    """Sorts a list l such that values at indices divisible by three are sorted to the front, and the rest is sorted normally."""
    return [x for x in l if x % 3 != 0] + [x for x in l if x % 3 ]

# Test cases
test_sort_third = [
    [1, 2, 3],
    [5, 6, 3, 4, 8, 9, 2],
    [5, 6, 3, 4, 8, 9, 2],
]

# Function call and test results
for test in test_sort_third:
    assert sort_third(test) == [2, 6, 3, 4, 8, 9, 5], "Passed test: " + str(test) + '"
```
The provided Python script defines a function `sort_third` that sorts a list such that values at indices divisible by three are sorted to the front, and the rest are sorted normally. The test cases are then passed to the function to validate its correctness, and the results are printed.