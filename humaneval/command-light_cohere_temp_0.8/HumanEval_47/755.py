```python
def median(lst):
    """Return median of elements in the list lst."""
    sorted_lst = sorted(lst)
    length = len(sorted_lst)
    if length % 2 == 0:
        return (sorted_lst[length // 2 - 1] + sorted_lst[length // 2]) / 2
    else:
        return sorted_lst[length // 2]

# Test cases
test_median = [
    dict(zip(median(['a',b,c']), ['a','b','c']))
    , (median([-10, 4, 6, 1000, 10, 20]), '10')
    , (median([-100, -200, 0, 200, 500, 600]), '100')
    ]

for test in test_median:
    assert median(test) == test[1]
```