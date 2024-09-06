```python
def median(l: list):
    """Return median of elements in the list l.
    l = sorted(l)
    n = len(l)
    middle = n // 2
    if n % 2 == 0:
        return (l[middle-1] + l[middle]) / 2
    else:
        return l[middle]

# Test case 1
assertEqual(median([3, 1, 2, 4, 5]), 3)

# Test case 2
assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15)

# Test case 3
assertEqual(median([10, -10, 4, 6, 1000, 20, 30]) , 15)
```