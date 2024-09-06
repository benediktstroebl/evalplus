```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
# Test case 1:
assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)
# Test case 2:
assertEqual(median([3, 1, 2, 4, 5]), 3.0)
# Test case 3:
assertEqual(median([5, 10, -10, 20, 6, 4]), 5.0)
```