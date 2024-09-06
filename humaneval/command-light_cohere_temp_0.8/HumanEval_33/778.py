```python
def sort_third(lst):
    """This function sorts a list l such that elements not divisible by three are at the beginning, and the rest are sorted normally.
    
    : [5, 6, 3, 4, 8, 9, 2]
    lst = [5, 6, 3, 4, 8, 9, 2]
    return sorted(lst,key=lambda x:int(x)%3)
```