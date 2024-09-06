```python
def median(l: list):
    """Return median of elements in the list l"""
    return (len(l) + 1) / 2 * sorted([x for x in l])[-1]

# Test cases
assertEqual(median([3, 1, 2, 4, 5]), 3.0)
assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)
assertEqual(median([10, 10, 10, 10]), 10.0)
assertEqual(median([1, 2, 3, 4, 5, 6]), 5.0)
assertEqual(median([6, 5, 4, 3, 2, 1]), 4.0)
assertEqual(median([60, 40, 30, 10, 20, 10]), 15.0)
assertEqual(median([21, 18, 10, 9, 26, 35, 36, 37]), 26.0)
assertRaises(median([3, -5, 8, -7, 6])),(3)
```