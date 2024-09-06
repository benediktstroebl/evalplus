```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    for num, count in dups.items():
        if count > 1:
            return False
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```

The function uses a simple dictionary (`dups`) to keep track of the occurrences of each number in the list. If there's a number more than once in the list, it will be in the dictionary with a count greater than 1, and hence `is_sorted` will return `False`. Otherwise, the list is iterated to check if it is ascending, and if so, it returns `True`.