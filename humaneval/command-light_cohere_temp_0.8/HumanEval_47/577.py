```python
def median(lst):
    """Return median of elements in the list lst."""
    if len(lst) < 1:
        raise ValueError("List is empty.
    if len(lst) == 1:
        return lst[0]
    mid = len(lst) // 2
    left = median(lst[:mid])
    right = median(lst[mid:])
    return (left + right) / 2

# Test the function
try:
    print(median([-10, 4, 6, 1000, 10, 20]))
except ValueError as ve:
    print(f"Error: {ve}")
```