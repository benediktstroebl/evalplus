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

The code exploits the fact that the returned list should have fewer characters in total, so we can use the `sum()` function to calculate the total number of characters in the strings of the two input lists and then compare them. The function returns the list with fewer characters, or the first list if the two lists have equal character counts.