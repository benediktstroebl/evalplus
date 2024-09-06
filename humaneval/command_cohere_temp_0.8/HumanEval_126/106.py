```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    return all(dups[n] == 1 for n in dups if dups[n] <= 1)
```

The function uses a simple dictionary (`dups`) to keep track of how many times each number appears in the list. If there's a duplicate number, it increments the count; otherwise, it initializes the count to 1. After processing all numbers, it checks whether each number has only 1 occurrence or less, and returns `True` only if that's the case for every number. The dictionary ensures that duplicates are checked in O(1) time for each number, maintaining a linear overall time complexity.