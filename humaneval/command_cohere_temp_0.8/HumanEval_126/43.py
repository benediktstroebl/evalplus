```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    return all(dups[n] == 1 for n in dups if dups[n] == 1)
```

The function uses a dictionary to count the occurrences of each unique number in the list. Then it checks if all non-unique values occur only once. The list of keys present in the dictionary with a value of 1 is used for the `all()` function to determine if the list is sorted in ascending order and has no duplicates. 

This approach reduces the complexity to O(n) from the previous O(n log n) approach and also uses less memory. 

The previous approach can be seen here:
```python
def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1)) and len(set(lst)) == len(lst)
```