```python
def sort_third(lst):
    """Returns a list l' where values at indices divisible by three are sorted, and other values are unchanged."""
    new_lst = []
    for i in range(len(lst)):
        if lst[i] % 3 == 0:
            new_lst.append(lst[i])
    else:
        new_lst.append(lst[i])
    new_lst.append(lst[i])
    return new_lst
#Example usage:
print(sort_third([1, 2, 3])) 
```