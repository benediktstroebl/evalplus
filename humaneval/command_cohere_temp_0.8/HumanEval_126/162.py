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
    return all(n < m for n, m in zip(lst, lst[1:]))
```

This function uses a dictionary, `dups`, to keep track of each unique element and its occurrence in the list. If any element occurs more than once, it's added to the dictionary with its count. After iterating through the list, the function checks if any key in the `dups` dictionary has a count greater than 1, and if so, it returns False, as the list has multiple duplicates. Otherwise, it proceeds to check if the list is sorted by comparing each element with the next one, and returns True if they are all in ascending order.