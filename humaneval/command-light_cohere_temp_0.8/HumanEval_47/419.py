```python
def median(lst):
    """Return median of elements in the list lst"""
    lst.sort()
   
    sorted(lst)
    length = len(lst)
    if length % 2 == 1:
        return (lst[-1] + lst[0]) / 2
    else:
        return lst[length // 2]

# Test cases
assert median([3, 1, 2, 4, 5]) == 3.0
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([1, 2, 3]) == 2.0
assert median([10, 20, 15, 30]) == 25
```