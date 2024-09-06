```python
def median(lst):
    """Return median of elements in the list lst."""
    if len(lst) < 1:
        raise ValueError("List must have at least 2 elements to compute median.")
    mid = len(lst) // 2 + 1
    l1, l2 = lst[:mid], lst[mid:]
    if l1 == l2:
        return (l1 + l2) / 2
    elif l1 > l2:
        return l1
    else:
        return l2

# Example usage
lst = [1, 2, 3, 4, 5]
print(median(lst))  # Output: 2.0
```