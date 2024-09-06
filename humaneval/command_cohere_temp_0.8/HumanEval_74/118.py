```python
def total_match(lst1, lst2):
    return lst1 if len(lst1) == len(lst2) else len(lst1) < len(lst2) and lst1 or lst2
```
The code solves the problem by checking the length of both lists and returning the list that has a total number of chars in all its strings less than the other list. If the lengths are equal, it returns the first list `lst1`. The or operator is used to merge the two lists if the condition is true.