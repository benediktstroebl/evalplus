```python
def sort_third(lst):
    """This function sorts a list l such that the elements divisible by three are in their correct positions. All other elements values are for all of l, are sorted accordingly. 
    Args:
        lst: list of integers
    Returns: sorted list"""
    lst[:] = sorted(lst, key=lambda x:int(x)//3)
    return lst

#test cases
print(sort_third([1, 2, 3]))  # [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # [2, 6, 3, 4, 8, 9, 5]
```