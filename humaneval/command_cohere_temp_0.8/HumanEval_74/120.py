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

The function compares the total number of characters in `lst1` and `lst2` and returns the list with fewer characters if the total is less. If both lists have the same number of characters, it returns the first list (`lst1`) if its length is shorter than the length of `lst2`, and `lst2` otherwise. The function handles these conditions through the summarized lengths of the lists and direct comparisons of their lengths.