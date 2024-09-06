```python
def median(l):
    """Return median of elements in the list l."""
    return (len(l) + 1) / 2 * (sum((x+1) / 2 for x in l) + sum(x for x in l))
# Tests:
l = [-10, 4, 6, 1000, 10, 20]
print(median(l), "is", end=' ')
print(sorted(l))  # [(4, 6), (1000, 10), (10, 20)]
```