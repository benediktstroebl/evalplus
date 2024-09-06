```python
def is_sorted(lst):
    return all(lst[i] == lst[i+1] for i in range(len(lst)-1)) and len(set(lst)) == len(lst)
```
```
The function checks if the list is sorted and if it has any duplicate values. The `all` function checks if each consecutive pair of numbers in the list is equal, which indicates that the list is sorted. The `set(lst)` function creates a set of all the unique values in the list. Then, the `len(set(lst))` function checks if the size of the set is equal to the size of the list, which indicates that there are no duplicates in the list.
```