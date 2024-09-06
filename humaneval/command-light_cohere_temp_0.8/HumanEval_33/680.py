```python
def sort_third(lst):
    """Sorts the list l such that elements divisible by three are moved last. Returns a last list with all elements divisible by three at the end."""
    lst[::3] = lst[-1:]
    return lst
# Test cases
test_sort = [1, 2, 3]
test_sort_empty = []
test_sort_odd = [5, 6, 3, 4, 8, 9, 2]

print(sort_third(test_sort))  # [2,3,1,2]
print(sort_third(test_sort_empty))  # []
print(sort_third(test_sort_odd))  # [2,6,3,4,8,9,5]
```