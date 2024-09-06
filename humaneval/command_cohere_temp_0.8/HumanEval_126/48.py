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

The function employs two conditional checks: the first identifies duplicate integers present multiple times in the list; the second checks if the integers are sorted in ascending order. The function returns True if the integers are sorted and have no duplicate entries larger than one; otherwise, it returns False.