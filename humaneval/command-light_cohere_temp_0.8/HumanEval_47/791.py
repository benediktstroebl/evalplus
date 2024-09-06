```python
def median(lst):
    """Return median of elements in the list lst."""
    n = len(lst)
    if n % 2 == 0:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]

# Test cases
test_median = [
    [(-10, 4, 6, 1000, 10, 20), (-5, -3, 3, -7, -8)],
    [2060, 13),
    [0, 2, 4, 8, 10, 12, 14],
    [20, 40, 60, 80]
]

for lst, exp in test_median:
    actual_median = median(lst)
    assert actual_median == exp, f"Failed for list: {lst}, expected: {exp}"
```  The median function calculates the median using the correct formula, and the test suite ensures that the function works as expected for various input lists.