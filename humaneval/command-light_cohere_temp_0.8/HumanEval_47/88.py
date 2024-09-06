```python
def median(lst):
    """Return the median of the list lst."""
    n = len(lst)
    if n % 2 == 1:
        return (l[n//2] + l[n//2 - 1]) / 2
    else:
        return l[n//2]

# Test cases
for i in range(0, 10):
    lst = [i, i*2, i*3, i*4]
    assert median(lst) == i*3

# Test case with negative numbers
lst = [10, 4, -6, 1000]
assert median(lst) == 6

# Test case with one element
lst = [1]
assert median(lst) == 1

# Test case with large list
lst = list(range(100001))
assert median(lst) == list(range(500))
```