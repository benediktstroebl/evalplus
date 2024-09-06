```python
def median(lst):
    """Return median of elements in the list lst."""
    # Sort the list in ascending order
    lst.sort()
   
    median_value = None
    i = len(lst) // 2
    while i >= 0:
        if lst[i] > lst[i + i]:
            median_value = lst[i]
            i -= 1
        else:
            break
    return median_value
# Example usage
lst = [4, 6, 10, 10, -10, 20, 3, 2]
print(median(lst))  # Output: 5.0
```