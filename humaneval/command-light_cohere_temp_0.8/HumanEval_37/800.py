```python
def sort_even(lst):
    even_lst = [x for x in lst if x % 2 == 0]
    even_val = [x for x in lst if x % 2 == 0]
    lst[:] = [x if x not in even_lst else even_val[even_lst.contains(x)]
    return lst
```

The function takes a list as input and returns a sorted list. It filters out even items from the list, which are even numbers and keeps them as they are in the original order. It then creates a list of even numbers and assigns this list to even_val. Then, it populates the list with elements from the original list, but only the elements which are not in even_lst are copied into lst. Finally, it returns the list.