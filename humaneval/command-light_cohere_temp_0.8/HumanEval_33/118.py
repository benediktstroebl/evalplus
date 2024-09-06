```python
def sort_third(lst):
    """This function sorts the list l such that values not divisible by three stay as they are, while values divisible by three are re-sorted so that their original order is restored. """"""
    important: It doesn't matter if the list is already sorted."""
    lst[:] = sorted(lst,key=lambda x:int(x)//3)
    return lst
# Test the function with various inputs.
print(sort_third([1, 2, 3]))          # [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2])) # [2, 6, 3, 4, 8, 9, 5]
```