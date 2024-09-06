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

The function employs a dictionary (`dups`) to keep track of the occurrences of each unique element in the input list (`lst`). If any element appears more than once in the list, the dictionary value will be greater than 1, and the function will return `False` since the list will not be considered sorted. Otherwise, the function returns `True` only if the sortedness condition is met, i.e., each element is less or equal to the next one in the list.