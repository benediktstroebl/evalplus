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

The function employs two nested conditions for its evaluation:
1. The outer condition `all(dups[num] == 1 for num in dups)` checks whether all elements in `dups` have a count of exactly 1, indicating the presence of no duplicates.
2. The inner condition `all(num < nums[1] for num, nums in dups.items())` checks whether all elements are sorted in ascending order. Here, `nums[1]` is utilized to denote the next element in line for comparison, assuming the list is sorted.

This approach allows the function to effectively determine whether a list is both sorted and free of duplicate elements.