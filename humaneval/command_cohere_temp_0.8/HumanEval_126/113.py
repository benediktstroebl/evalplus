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
The function first checks for duplicates and ensures no item appears more than once in the list. It then checks whether the list is monotonically increasing using a simple linear traversal and comparison. The function returns False if any duplicate is found, and True if no duplicates are present and the list is sorted.