```python
def median(l: list):
    """Return median of elements in the list l.
    l = [list](l) # check if list is valid
    if len(l) < 1:
        raise ValueError("List cannot be empty")
    if len(l) == 1:
        return l[0]
    mid = len(l) // 2
    left = median(l[:mid])
    right = median(l[mid:])
    return (left + right) / 2
# test cases
median([-10, 4, 6, 1000, 10, 20])
median([3, 1, 2, 4, 5])
median([100, 200, 3, 4, 5])
median([0, -10, 4, 6, 7]) # negative numbers test
median([9, 2, 1]) # single element list
```