```python
def sort_third(lst):
    """This function sorts a list l such that all the numbers divisible by three are in their correct relative order.
    Numbers that are not divisible by three stay in their original relative order. Numbers that are divisible by three are equal to the corresponding values of l, but are sorted.
    Args:
    lst (list)
    Returns:
    list l' such that all the numbers in l are in their correct relative order."""
    lst[::3] = lst[::3].copy()  # i.e the numbers in thes, all the numbers divisible by three in their correct order and are the same for the numbers that are not divisible by three.
    lst[:-3] = lst[:-3].copy()  # i.e is in the relevant.
    lst = lst[::3]
    return lst
# Test the function
test_list = [5, 6, 3, 4, 8, 9, 2]
result = sort_third(test_list)
assert result == [2, 6, 3, 4, 8, 9, 5]
```