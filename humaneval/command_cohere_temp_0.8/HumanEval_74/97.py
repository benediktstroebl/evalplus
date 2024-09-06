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

The solution utilizes twosum to determine the total character count of both lists, confirming whether one list has more characters than the other. If so, it returns the list with fewer characters. To handle equal character counts, it returns the first list if it's shorter or the second list if it's longer. This logic ensures concise and efficient list reconciliation.