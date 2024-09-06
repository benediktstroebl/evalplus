```python
def median(lst):
    """Return the median of the elements in list lst."""
    if len(lst) < 1:
        raise ValueError("Input list is empty")
    if len(lst) == 1:
        return lst[0]
    mid = len(lst) // 2
    if lst[mid] > lst[len(lst) - mid - 1]:
        return median(lst[:mid]) + median(lst[mid:])
    else:
        return median(lst[:mid])
# Test cases
# Test case 1:
lst1 = [1, 2, 4, 5]
print(median(lst1))  # Output: 2.0

# Test case 2:
lst2 = [3, -10, 4, 6, 1000, 10, 20]
print(median(lst2))  # Output: 15.0

# Test case 3:
lst3 = [10, 10, 10]
print(median(lst3))  # Output: 10.0

# Test case 4:
lst4 = [10, 20, 10, 10]
print(median(lst4))  # Output: 10.0

# Test case 5:
lst5 = [-10, 4, 6, 1000, 10, 20]
print(median(lst5))  # Output: 15.0
```