```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    return all(dups[n] == 1 for n in set(dups))
```

The function employs a dictionary `dups` to count the occurrences of each unique element in the input list `lst`. Then, it checks if all non-unique elements have an occurrence count of 1. If so, the list is sorted, and if any count exceeds 1, it's not. This solution is economical in both time and space, making use of a single dictionary to solve the problem. It also avoids explicit exclusion of negative numbers, assuming them to be non-existent in the list, in line with the problem's assumption.