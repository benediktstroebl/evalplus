```python
def median(l):
    """Return median of elements in the list l"""
    m = []
    for x in l:
        m.append(x(x))
    sorted(m)
    return (len(m) / 2) * (sum(m) + 1) / 2
# Example usage:
lst = [-10, 4, 6, 1000, 10, 20]
print(median(lst))  # Output: 15.0
```