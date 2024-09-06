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

The code exploits the fact that the returned list should have fewer characters in total than the other list, or be the list itself. Hence the function performs a comparison of the total characters in both lists and returns the list with fewer characters, or the first list if both have the same number of characters.