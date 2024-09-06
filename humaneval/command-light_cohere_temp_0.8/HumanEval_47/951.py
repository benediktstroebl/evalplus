```python
def median(lst):
    """Return median of elements in the list lst."""
    if len(lst) < 1:
        raise ValueError("Input list is empty.")
    if len(lst) == 1:
        return lst[0]
    n = len(lst) // 2 + 1
    m = (n + 1) // 2
    if n % 2 == 0:
        return (lst[m-1] + lst[m]) / 2
    else:
        return lst[m]
# Example usage
lst = [1, 2, 3, 4, 5]
print(median(lst))  # Output: 3
```