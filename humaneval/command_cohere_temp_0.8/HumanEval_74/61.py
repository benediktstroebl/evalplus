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

The solution utilizes two sum totals for comparison. It also includes a tiebreaker, resorting to the shortest list. The solution works for cases like empty lists and single elements. 

This algorithm optimizes computational complexity by calculating total characters only once for each list, resulting in O(n) where n is the length of the longest list.

Unit tests:
```python
test_total_match = ({'lst1': ['hi', 'admin'], 'lst2': ['hI', 'Hi']}, ['hI', 'Hi'])
(truth, result) = test_total_match
assert result == total_match(truth['lst1'], truth['lst2'])
``` 

Expected output: `['hI', 'Hi']`