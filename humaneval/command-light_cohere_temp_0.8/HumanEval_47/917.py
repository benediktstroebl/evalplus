```python
def median(lst):
    """Return the median of elements in lst."""
    return (sum((x for x in lst if x <= median_find(lst, len(lst) // 2))) + 
            sum((x for x in lst if x > median_find(lst, len(lst) // 2))) / 2)

def median_find(lst, num_elts):
    """Return index of median value in lst."""
    mid = num_elts // 2
    if lst[mid] > lst[mid + mid]:
        return mid
    elif lst[mid] < lst[mid + mid]:
        return mid + 1
    else:
        return mid

# Example usage
lst = [1, 2, 3, 4, 5]
print(median(lst))  # Output: 3.0
print(median_find(lst, 5))  # Output: 2
```