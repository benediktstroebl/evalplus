```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that l' is identical to l, except the values divisible by three are sorted to appear last.
    lst[:] = [num for num in lst if num % 3 != 0]
    lst = sorted(lst)
    lst[-1:] = lst.return = lst[index]
    lst = lst[1:] + lst[:-index]
    return lst
```