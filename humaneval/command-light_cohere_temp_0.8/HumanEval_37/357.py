```python
def sort_even(lst):
    """This function sorts the list of integers in the list l such that the values of the even index of the list
    are equal to each other but sorted.
    The list of the odd index values of the list l are sorted.
    The list of even items of the list l are sorted.
    """
    expected output:
    [3, 2, 1, 4, 5, 6]
    """
    lst = [3, 2, 1, 4, 5, 6]
    lst = sorted(set(lst))
    return [x for x in lst if x in [3, 4]]
```