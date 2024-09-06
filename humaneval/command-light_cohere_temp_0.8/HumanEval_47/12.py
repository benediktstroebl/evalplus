```python
def median(l: list):
    """Return median of elements in the list l.
    assert len(l)==len(set(l)), "Same elements in list"
    assert l[:len(l)//2] == l[len(l)//2:], "List not sorted"
    return (l[len(l)//2] + l[len(l)//2-1]) / 2

# Example usage
lst = [-10, 4, 6, 1000, 10, 20]
print(median(lst))  # Output: 15.0
```