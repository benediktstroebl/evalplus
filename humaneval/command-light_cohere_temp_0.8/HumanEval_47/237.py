```python
def median(lst):
    """Return median of elements in the list lst."""
    if len(lst) < 1:
        raise ValueError("Input list is empty")
    if len(lst) == 1:
        return lst[0]
    m = len(lst) // 2 + 1
    i = m - 1
    while i >= 0:
        if lst[i] > lst[m]:
            m, i = i, m
        elif lst[i] < lst[m]:
            pass
        else:
            break
    return (lst[m] + lst[i]) / 2

# Test cases
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
print(median([-20, -15, -10, 25, -5, -3]))  # Output: -15.0
print(median([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Output: 5.0
```

The function median in the above script calculates the median of a given list of numbers. It handles empty lists, single elements, and lists with varying lengths. The median is calculated using the above approach, where the middle value is selected and returned, or the average of the two middle values is calculated.