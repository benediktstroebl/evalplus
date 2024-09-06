```python
def sort_third(lst):
    """Sorts a list l such that values not divisible by three are at the beginning"""
    lst[::3] = lst[::3].copy()
    lst.apply_sort()
    providersort = list(range(len(lst), 0, -1, 3))
    lst = lst[:] + lst[3:]
    return lst

# Example
my_list = [5, 6, 3, 4, 8, 9, 2]
print(sort_third(my_list))  # [2, 6, 3, 4, 8, 9, 5]
```