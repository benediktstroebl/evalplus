```python
def median(l: list):
    """Return median of elements in the list l."""
    n = len(l)
    if n % 2 == 0:
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        return l[n // 2]
```
The function `median` takes a list `l` as input and returns the median of its elements. This is also handles the example provided correctly:
- For an even number of elements, it returns the average of the two middle elements.
- For an single middle element for an odd number of elements.

This self-contained function demonstrates the use of Python's built-in list functions and basic mathematical operations.