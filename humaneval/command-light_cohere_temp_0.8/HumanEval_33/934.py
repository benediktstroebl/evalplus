```python
def sort_third(lst):
    """Sorts the list l such that elements divisible by three are in their correct relative order."""
    mys = sorted(lst, key=lambda x: x // 3)
    return mys

# Test
my_list = [5, 6, 3, 4, 8, 9, 2]
print(sort_third(my_list))  # [2, 6, 3, 4, 8, 9, 5]
```