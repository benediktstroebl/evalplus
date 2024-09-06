```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    return all(dups[n] == 1 for n in dups if dups[n] != 1)
```

The function uses a simple dictionary (`dups`) to keep track of how many times each number appears in the list. If any number appears more than once and the count is not 1, it returns `False`. If the count is 1 for all numbers, it returns `True`.