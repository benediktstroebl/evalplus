```python
def median(lst):
    """Return median of elements in the list lst"""
    lst.sort()
    | m = [float(x) for x in sorted(lst, reverse=True)]
    return 0.5 + (len(lst) + 1) * (m[len(m)//2] + m[(len(m)//2)+1]) / 2
```
This function takes a list as an argument and returns the median value of the elements in that list. It achieves this by sorting the elements in ascending order and then calculating the median using the formula you provided.