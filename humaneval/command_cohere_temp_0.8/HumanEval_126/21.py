```python
def is_sorted(lst):
    dups = {}
    for x in lst:
        if x in dups:
            dups[x] += 1
        else:
            dups[x] = 1
    
    for num in dups:
        if dups[num] > 1: 
            return False
    
    return lst == sorted(lst)
```

The function works by first checking if any elements in the list occur more than once. If so, it returns false immediately since duplicates aren't allowed in sorted lists. Otherwise, it compares the list against a sorted version of itself. If they are the same, then the list is sorted with no duplicates, and the function returns true, otherwise it returns false. This works for the provided test cases and should have a reasonable time complexity of O(n log n) due to the sorting required.