```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    for n, cnt in dups.items():
        if cnt > 1:
            return False
    return len(set(lst)) == len(lst) and all(n <= m for n, m in zip(lst, lst[1:]))
```

This function checks if a list of numbers is sorted in ascending order, ignoring duplicate values. It uses a dictionary, `dups`, to track each unique number's occurrence count. If any number appears more than once, the function returns `False`. 

Otherwise, it compares each element once with the next one, returning `True` if they are non-decreasing. Also, the function ensures the list has no duplicates, checking that its length matches the set's. This optimized approach efficiently solves the problem in a single function, achieving a time complexity of O(n).