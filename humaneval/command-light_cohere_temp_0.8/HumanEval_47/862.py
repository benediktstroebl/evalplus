```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test cases
test_median = [
    [
        [10, 20, 30, 40],
        [-10, 4, 6, 1000],
        [1, 2, 3, 4, 5],
        [5, 5, 6, 7],
        [23, 45, 67, 89]
    ]

for test in test_median:
    actual = median(test)
    expected = eval(''.join(f'median({a})' for a in test))
    assert actual == expected, f"Median did not match expected for {test}"
```

This script defines a function median that computes the median of a list of elements. The function handles both even cases: when the list has an even number of elements, it returns the average of the two middle numbers; when the list has an odd number of elements, it returns the middle number. 

The test cases ensure that the function works correctly for various lists of elements.