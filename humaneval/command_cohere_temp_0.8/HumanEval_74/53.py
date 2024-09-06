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

The function compares the total number of characters in `lst1` and `lst2` and returns the list with fewer characters if the total character count is different. If the total character count is the same or both lists have the same length, the function returns `lst1` if its length is less than `lst2`, and `lst2` otherwise. This strategy ensures that the function adheres to the problem statement's guidelines, prioritizing returning the list with fewer characters and defaulting to the shorter list if counts are equal.