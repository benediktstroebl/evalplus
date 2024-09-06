```python
def sort_third(lst):
    """Sorts the list l such that values at indices divisible by three are sorted equal, and other values are sorted as default.
    
    Args:
        lst (list): list to be sorted

    Returns:
        sorted list lst
    """
    lst[:] = sorted(lst, key=lambda x: x // 3) + [x for x in lst if x % 3 != 0]
    return lst
```
Test your function using some test cases. You can add more test cases to this script.