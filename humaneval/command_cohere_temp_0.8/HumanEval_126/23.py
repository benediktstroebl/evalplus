```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    return all(dups[n] == 1 for n in dups if dups[n] == 1) and all(n<m for n,m in zip(lst, lst[1:]))
```
The function uses a dictionary (`dups`) to count the number of duplicates for each element in the list. Then, it checks whether all distinct elements have only one occurrence and whether all elements are in ascending order. The `all()` function is used to check both conditions, `all(dups[n] == 1 for n in dups if dups[n] == 1)` checks whether there are no duplicates, and `all(n<m for n,m in zip(lst, lst[1:]))` checks whether the list is sorted.