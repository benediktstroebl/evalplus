```python
def median(lst):
    """Return median of elements in the list lst"""
    if len(lst) % 2 == 0:
        return (lst[(len(lst) / 2) - 1] + lst[len / 2]) / 2
    else:
        return lst[len // 2]

# Test cases
for i in range(0, 10):
    lst = [i, i*2, i*3, i*4]
    assert median(lst) == i*3
```