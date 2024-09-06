```python
def sort_third(lst):
    """Sorts a list l such that all items not divisible by three are at the beginning, and all items divisible by three are at the end."""
    return lst[::-1] if len(lst) > 1 and all(i % 3 for i in lst) else lst
```
The above function takes a list lst as input and returns a new list lst' such that all the values in lst that are not divisible by three will be at the beginning (index of 0), while all the values that are divisible by three will be at the end (index of len(lst)-1).