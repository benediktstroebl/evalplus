```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    return all(dups[n] == 1 for n in dups if dups[n] == 1)
```

The function uses a dictionary to count the occurrences of each unique element in the input list. Then it checks if all non-duplicate elements have only one occurrence, which means the list is sorted with no duplicates, hence it returns True. Otherwise, at least one element has more than one occurrence, meaning there are duplicates, so it returns False.