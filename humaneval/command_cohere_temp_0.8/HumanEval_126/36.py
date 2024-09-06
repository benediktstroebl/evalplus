```python
def is_sorted(lst):
    dups = {}
    for x in lst:
        if x in dups:
            dups[x] += 1
        else:
            dups[x] = 1
    for x in dups:
        if dups[x] > 1:
            return False
    return True
```

The function employs a simple algorithm that iterates over the list of integers. It checks for each integer in the list whether it's encountered before, storing the occurrence count in the `dups` dictionary. After processing the entire list, the function checks if any integer appears more than once, returning `False` if so. If no duplicate occurrence is found, it returns `True`, indicating that the list is sorted. 

This algorithm's efficiency is proportional to the list's size, providing a linear time solution.