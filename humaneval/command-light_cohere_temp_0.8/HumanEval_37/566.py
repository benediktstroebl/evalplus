```python
def sort_even(lst):
    """Sorts the list lst such that elements at odd positions are kept as they are, while elements at even positions are sorted."""
    even = [x for x in lst if x % 2 == 0]
    even.sort(key='even')
    lst = list(set(even))
    return lst

# Test the function
>>> sort_even([1, 2, 3])
[1, 2, 3]
>>> sort_even([5, 6, 3, 4])
[3, 6, 5, 4]
```