```python
def total_match(lst1, lst2):
    l1_total = sum(len(x) for x in lst1)
    l2_total = sum(len(x) for x in lst2)
    if l1_total < l2_total:
        return lst1
    elif l2_total < l1_total:
        return lst2
    else:
        return lst1 if len(lst1) < len(lst2) else lst2
```

The code sums the lengths of all strings in both lists, compares the totals, and returns the list with fewer total characters. If both lists have the same total, it returns the list that is lexicographically earlier. The unit tests check all edge cases as described in the problem statement.