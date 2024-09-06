```python
def total_match(lst1, lst2):
    total1 = sum(len(x) for x in lst1)
    total2 = sum(len(x) for x in lst2)
    if total1 > total2:
        return lst2
    elif total2 > total1:
        return lst1
    else:
        return lst1 if len(lst1) < len(lst2) else lst2
```

The code sums the lengths of all strings in both lists, comparing the totals. If one list has a shorter total length, it's returned. If both are equal, the list with fewer strings is returned. The algorithm is concise and efficient, fulfilling the specified requirements and passing all test cases.