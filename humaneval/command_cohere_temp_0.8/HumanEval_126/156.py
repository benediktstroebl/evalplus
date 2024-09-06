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

The function employs two iterative loops: the first to check for duplicates and count their occurrences, and the second to check if the list is sorted. After counting duplicates, it returns False if any count greater than 1, indicating not sorted. Otherwise, it returns True, assuring the list is sorted and has only single duplicates, or no duplicates at all. 

This approach does not require any additional modules and can be run directly in Python. It also allows for a straightforward comprehension of the problem and delivers a concise solution. 

The total time complexity of this code is O(n), where 'n' is the length of the input list 'lst'.