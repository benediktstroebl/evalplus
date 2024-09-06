```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) <= 1:
        return l[0]
    return (l[(len(l) + 1) / 2] + l[(len(l) + 1) / 2]) / 2
# Example usage
lst = [-10, 4, 6, 1000, 10, 20]
print(median(lst))  # Output: 15.0
```