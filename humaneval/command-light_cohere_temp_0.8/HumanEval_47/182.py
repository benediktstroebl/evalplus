```python
def median(l):
    """Return median of elements in the list l."""
    # Sort the list
    l.sort()
    median = float('inf')
    for i in range(len(l)//2):
        median = l[i] + l[len(l)-i-1] / 2
    return median
# Unsorted list
median([-10, 4, 6, 1000, 10, 20])
# Unsorted list
median([3, 1, 2, 4, 5])
# Unsorted list
median([100, 1000, 200])
# Sorted list
median([-10, 4, 6, 1000, 10, 20])
# Sorted list
median([3, 1, 2, 4, 5])
```