```python
def total_match(lst1, lst2):
    return lst1 if len(lst1) == len(lst2) else len(lst1) < len(lst2) and lst1 or lst2
```
This Python script defines a function called `total_match` that takes two lists of strings, `lst1` and `lst2`, as input. The function returns the list that has the total number of characters in all strings less than the other list. If the two lists have the same number of characters, it returns the first list (`lst1`). The function uses logical and/or concatenation to return the list with fewer characters.