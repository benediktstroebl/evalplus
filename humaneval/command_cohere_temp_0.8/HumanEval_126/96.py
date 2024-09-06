```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    
    for num, dup in dups.items():
        if dup > 1: 
            return False
    
    return lst == sorted(lst)
``` 

The function uses a simple dictionary, `dups`, to track occurrences of each number in the list. If any entry in `dups` is greater than 1, there are duplicates, and the list is not sorted. If no duplicates exist, the list is sorted.