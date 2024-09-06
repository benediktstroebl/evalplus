```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    return all(dups[num] == 1 for num in dups) and all(num < nums[1] for num, nums in dups.items())
```

The function employs two conditional checks:
1. The first conditional check employs the `all()` function to verify if all values in the list are unique, denoted by `dups[num] == 1`.
2. The second conditional check employs the `all()` function to verify if all the elements are sorted in ascending order, denoted by `num < nums[1]` with `nums` being the list of occurrences of the current element `num`.

The function returns `True` if all these conditions are met, and `False` otherwise.