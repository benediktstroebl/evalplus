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

The function uses a dictionary to count the number of times each element appears in the list and verifies two conditions:
1. Whether each element in the list appears only once (via `all(dups[num] == 1 for num in dups)`)
2. Whether the elements are sorted in ascending order (via `all(num < nums[1] for num, nums in dups.items())`). 

The function will return True if both conditions are satisfied and the list is sorted with no duplicates. Otherwise, it returns False.