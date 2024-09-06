```python
def median(lst):
    """Return median of elements in the list lst"""
    n = len(lst)
    if n % 2 == 0:
        return (lst[(n // 2 - 1) : n // 2 + 1]) + (lst[n // 2])
    else:
        return lst[(n // 2)]

# Test cases
test_median = [
    [
        [],
        [10, 20, 30],
        [1000, 4000, 6000],
        [-10, 4, 6, 8, 90],
        [1, 2, 3, 4, 5]
    ]
)

for test in test_median:
    actual_median = median(test)
    expected_median = [10, 15, 20, 5]
    print(f"Test: [{test}], Actual: {actual_median}, Expected: {expected_median}")
    assert actual_median == expected_median, f"Test [{test}] failed"
```