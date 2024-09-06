```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that the list l' is sorted so that all values that are divisible by three appear in their correct positions.
    
    Args:
        lst (list) -> input list
    """
    lst = sorted(lst, key=lambda x:int(x) % 3)
    return lst
```