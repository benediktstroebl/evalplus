```python
def median(lst):
    """Return median of elements in the list lst."""
    if len(lst) == 0:
        raise ValueError("Input list cannot be empty")
    if len(lst) % 2 == 0:
        return (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2
    else:
        return lst[len(lst) // 2]

# Test the median function
lst1 = [3, 1, 2, 4, 5]
assert median(lst1) == 3.2
lst2 = [1, 2, 3, 4, 5, 6]
assert median(lst2) == 3.2
lst3 = [10, 20, 40, 30, 10]
try:
    median(lst3)
except ValueError as e:
    print(f"Median for input list lst3 raised error: {e}")
```