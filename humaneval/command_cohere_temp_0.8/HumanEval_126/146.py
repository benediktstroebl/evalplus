```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    for num, count in dups.items():
        if count > 1:
            return False
    return len(lst) <= 1 or lst == sorted(lst)
```

This function checks if there are any elements in the list that appear more than once, keeping track of duplicates and their counts in the `dups` dictionary. If any element appears more than once, it returns `False` since such a list cannot be sorted. Otherwise, it checks if the length of the list is 1 or if the list is sorted in ascending order, returning `True` if either of these conditions is met. This solution encompasses the examples given in the problem statement.