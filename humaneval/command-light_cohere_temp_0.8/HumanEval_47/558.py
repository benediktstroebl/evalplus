```python
def median(lst):
    """Return the median of elements in the list lst."""
    sorted_lst = sorted(lst)
    n = len(sorted_lst)

    if n % 2 == 1:
        return (sorted_lst[n//2 - 1] + sorted_lst[n//2]) / 2
    else:
        return sorted_lst[n//2]

# Test cases
for i in range(0,10):
    lst = list(range(i,i+10))
    assert median(lst) == float(i+3.5)
```