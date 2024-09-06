```python
def median(l: list):
    """Return median of elements in the list l."""
    l = list(map(float, l))  # Convert list to float to perform calculations
    m = [x for x in l if x == l[len(l) // 2]]
    return sum(m) / 2
```