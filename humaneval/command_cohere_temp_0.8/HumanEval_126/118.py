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

The function uses a simple dictionary (`dups`) to keep track of how many times each number appears in the list. If there's a duplicate number, it increments the count; otherwise, it initializes the count to 1. After processing all numbers, it checks whether each number has only a single occurrence (`dups[n] == 1`) - if so, the list is sorted with no duplicates, and if not, it is not sorted with duplicates. Using `all()` returns `True` if all conditions are met, i.e., if all duplicate numbers have only one occurrence, indicating a valid sorted list with no duplicates.