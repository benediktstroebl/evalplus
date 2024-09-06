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
The function `is_sorted` checks for duplicates in the list using a dictionary `dups` to track occurrences of each unique item. If any item appears more than once, it immediately returns `False`. After processing, if no duplicates are found, it checks if the list is monotonically increasing (i.e., sorted) and returns `True` if so, and `False` otherwise. The markdown code block above provides a complete Python script to solve the problem.  This solution has a time complexity of O(n) and a space complexity of O(n). It handles all the edge cases as specified in the provided examples.