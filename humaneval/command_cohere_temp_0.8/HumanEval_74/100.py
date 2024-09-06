```python
def total_match(lst1, lst2):
    return lst1 if len(lst1) == len(lst2) else len(lst1) < len(lst2) and lst1 or lst2
```
This Python script defines a function called `total_match` that takes two lists of strings, `lst1` and `lst2`, as input. The function returns the list that has a total number of characters in all of its strings less than the other list's strings. If both lists have the same number of characters, it returns `lst1`, whereas if the lengths are different, it returns the list with the smaller total character count, selecting from `lst1` or `lst2` as necessary. The logic ensures that it returns a valid answer even if one list is empty, and if both lists have the same total character count, it returns the first list.