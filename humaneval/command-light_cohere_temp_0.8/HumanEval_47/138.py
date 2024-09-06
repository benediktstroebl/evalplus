```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) < 1:
        return None  # Handle empty list
    middle = len(l) // 2
    if len(l) % 2 == 0:
        return (l[middle - 1] + l[middle]) / 2
    else:
        return l[middle]

# Test cases
assertEqual(median([3, 1, 2, 4, 5]), 3)
assertEqual(median([-10, 4, 6, 1000, 10, 20]), 10)
assertEqual(median([1, 2, 4, 8, 5, 6]) , 5)
assertEqual(median([-100, -200, -300, -40, -100, -500, 20, 50, 400]) , -300)
assertEqual(median([10, 20, 30, 40]) , 40)
```