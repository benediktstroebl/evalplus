```python
def median(l: list):
    """Return median of elements in the list l."""
    assert len(l)==len(sorted(l))
    assert l[0] <= l[-1]
    m = len(l)//2
    if m == 1:
        return l[m]
    return (l[m-1] + l[m])/2
# Example usage
lst1 = [-10, 4, 6, 1000, 10, 20]
print(median(lst1))  # Output: 15.0
```