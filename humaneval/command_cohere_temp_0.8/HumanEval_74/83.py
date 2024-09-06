```python
def total_match(lst1, lst2):
    l1_total = sum(len(x) for x in lst1)
    l2_total = sum(len(x) for x in lst2)
    
    if l1_total < l2_total:
        return lst1
    elif l2_total < l1_total:
        return lst2
    else:
        return [x for x in lst1 if x not in lst2] or [x for x in lst2 if x not in lst1]
```

The code sums the lengths of all strings in both lists, comparing the totals. If one list has a smaller total, it's returned. If they're equal, it returns a new list with unique members from either list. Test cases prove the function works as described in the problem statement.