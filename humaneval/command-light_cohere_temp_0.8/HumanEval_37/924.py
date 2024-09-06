```python
def sort_even(lst):
    """Sorts a list l such that all elements at odd positions are kept unchanged, and elements at even positions are sorted.
    Args:
        lst (list) : list of elements to be sorted
    Returns:
        lst : sorted list
    """
    lst[:] = lst[1:]  # copy the list and remove the first element (the largest odd element)
    even = [x for x in lst if x % 2 == 0]
    lst = [x for x in lst if not in even] + even
    return lst

# test cases
print(sort_even([1, 2, 3]))       # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))    # [3, 6, 5, 4]
print(sort_even([10, 20, 30, 10])) # [10, 20, 30, 10]
```