```python
def median(lst):
    """Return the median of elements in list lst."""
    return (len(lst) + 1) / 2 * (lst[len(lst) // 2] + lst[len // 2])

# Test cases
for i in range(0, 5):
    print(median([10, 20, i, 4, 6]))  # Output should be 5.0
```