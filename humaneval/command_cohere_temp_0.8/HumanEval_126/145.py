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

The function uses a simple dictionary (`dups`) to keep track of how many times each number appears in the list. If any number appears more than once and it's not the only occurrence in the list, the function will return `False`. Otherwise, it returns `True`.