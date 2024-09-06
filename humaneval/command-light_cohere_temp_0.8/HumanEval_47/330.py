```python
def median(l: list):
    """Return median of elements in the list l"""
    assert len(l) > 1, "Input list must have at least two elements"
    middle = len(l) // 2
    if len(l) % 2 == 0:
        return (l[middle-1] + l[middle]) / 2
    else:
        return l[middle]
#Example usage
med = median([-10, 4, 6, 1000, 10, 20])
assert med == 15.0
 ```