```python
def is_sorted(lst):
    return sorted(lst) == lst 

# Test the function
is_sorted([5])  # True
is_sorted([1, 2, 3, 4, 5])  # True
is_sorted([1, 3, 2, 4, 5])  # False
is_sorted([1, 2, 3, 4, 5, 6])  # True
is_sorted([1, 3, 2, 4, 5, 6, 7])  # True
is_sorted([1, 3, 2, 4, 5, 6, 7])  # False
is_sorted([1, 2, 2, 3, 3, 4])  # True
is_sorted([1, 2, 2, 2, 3, 4])  # False
# The list with duplicate elements is always considered unsorted
```