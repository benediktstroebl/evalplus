```python
def sort_third(l: list):
    """Sorts list l such that values at indices divisible by three are in l's final values, and the other values are in their original order.
    
    Args:
        l (list): list to be sorted
    """
    # Sort the list without regards to divisibility by three
    l = sorted(l)
    # Remove values divisible by three from the sorted list
    l = [x for x in l if x % 3 != 0]
    return l
```