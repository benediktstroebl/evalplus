```python
def median(l: list):
    """Return median of elements in the list l."""
    return (len(l) + 1) / 2.0  # .5 *l[::len(l) - 1])

# Test the function with different inputs
assert(median([3, 1, 2, 4, 5]) == 3.0)
assert(median([-10, 4, 6, 1000, 10, 20]) == 15.0)
assert(median([2, 4, 6, 8, 10]) == 5.0)
assert(median([14, 19, 22, 12, 15]) == 12.0)
```