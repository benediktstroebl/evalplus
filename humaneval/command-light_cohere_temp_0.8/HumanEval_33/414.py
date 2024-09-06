```python
def sort_third(lst):
    """Sorts a list l such that all numbers divisible by three appear first, and the rest in their original order.
    
    Args:
        lst (list): list of numbers
    """
    lst[:] = sorted(lst, key=lambda x: x % 3)
    return lst
```