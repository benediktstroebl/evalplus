```python
def median(l: list):
    """Return median of elements in the list l"""
    return (len(l) + 1) / 2 * (sum((x + 1) / 2 for x in l) + sum(x for x in l))

#Test cases
assert median([3, 1, 2, 4, 5]) == 3
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([]) == 0
```