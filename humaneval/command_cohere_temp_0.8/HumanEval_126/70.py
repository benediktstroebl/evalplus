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

This function first checks for duplicates and makes sure there are no duplicates greater than 1; then it checks if the list is monotone increasing to determine if the list is sorted. The script passes the provided test cases as it returns True for the examples given and False appropriately.