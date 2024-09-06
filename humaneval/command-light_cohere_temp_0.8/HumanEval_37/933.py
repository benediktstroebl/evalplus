```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even index of l, but sorted."""
    return sorted(l, key = lambda x:x if x%2 == 0 else x -1 )
```
The output of this script will be a sorted list with the odd index and even index values of an input list.