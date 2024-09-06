```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    return all(dups[num] == 1 for num in dups if dups[num] != 1)
```

The function employs a simple logic where it checks for the count of duplicates in the list against the condition that any duplicate counts to be greater than 1 will lead to False, and if none of the counts are greater than 1, True is returned.