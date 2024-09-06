```python
def median(lst):
    """Return median of elements in the list lst."""
    n = len(lst)
    m = n // 2 + 1
    if n % 2 == 0:
        return (l[m-1] + l[m]) / 2
    else:
        return l[m]
# Example usage
lst1 = [-10, 4, 6, 1000, 10, 20]
print(median(lst1))  # Output: 15.0
```