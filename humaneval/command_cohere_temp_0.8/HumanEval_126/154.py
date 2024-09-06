```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    for n, count in dups.items():
        if count > 1:
            return False
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```
The function uses a simple dictionary (`dups`) to count the number of duplicates in the list. If there's any element with a count greater than 1, it's not sorted. If there are no duplicates, it checks if the list is numerically sorted in ascending order, and returns `True` if so. The markdown code block at the beginning is included for context.