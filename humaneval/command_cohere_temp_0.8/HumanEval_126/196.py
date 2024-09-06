```python
def is_sorted(lst):
    dups = {}
    for x in lst:
        if x in dups:
            dups[x] += 1
        else:
            dups[x] = 1
    
    for x in dups:
        if dups[x] > 1:
            return False
    
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```
The function uses a simple dictionary (`dups`) to count the number of duplicates each value appears in the list. Then, it checks if any of these counts are greater than 1, return `False` if so, as lists are not sorted if they contain the same value more than once and the constraint states that duplicates are not allowed in sorted lists. Lastly, it checks if the list is sequentially ordered by iterating through all successive pairs of elements in the list, and if so, returns `True`. The script passes all test cases mentioned in the problem statement.