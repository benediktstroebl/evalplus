```python
def sort_third(lst):
    """Returns a list l' such that all items in l' are the items from l that are not divisible by three.
    If the numbers divisible by three are equal to the corresponding items from l, but sorted."""
    lst[::3] = lst[::3].copy()
    return lst
# Test the function with sample inputs
test_list = [5, 6, 3, 4, 8, 9, 2]
result = sort_third(test_list)
assert result == [2, 6, 3, 4, 8, 9, 5]
```