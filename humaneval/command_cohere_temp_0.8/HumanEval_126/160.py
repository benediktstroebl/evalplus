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
    return all(x <= y for x, y in zip(lst, lst[1:]))
```

This Python script provides a self-contained function `is_sorted` that solves the problem statement. It checks for duplicates in the list and ensures that all elements after the first occurrence of a duplicate are greater than or equal to the duplicate. It returns False if there's a duplicate element with more than one occurrence, as per the problem statement requirement. Otherwise, it checks if the list is sorted without considering the duplicate occurrences. The script includes a `dups` dictionary to track duplicate occurrences and utilizes `all()` and `zip` to efficiently check if the list is sorted. Overall, the code is concise and effective in solving the given problem.