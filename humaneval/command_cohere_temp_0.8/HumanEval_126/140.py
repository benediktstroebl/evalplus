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

The function uses a dictionary to count the number of duplicates of each number in the list. Then it checks if all non-duplicate numbers have only 1 occurrence. The set of numbers serves to eliminate duplicate checks for duplicate numbers.