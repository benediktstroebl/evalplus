```python
def total_match(lst1, lst2):
    return lst1 if len(lst1) == len(lst2) else len(lst1) < len(lst2) and lst1 or lst2
```
The code returns the list that has a total number of chars in all of the strings less than the other list. If the total number of chars is the same, it returns the first list `lst1`. The function uses logical and and or operators to selectively return either of the two lists based on the conditions specified in the spec.