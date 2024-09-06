```python
def total_match(lst1, lst2):
    return lst1 if len(lst1) == len(lst2) else len(lst1) < len(lst2) and lst1 or lst2
```
The code returns the list that has a total number of characters in its strings less than the other list. If the total number of characters is the same, it returns the first list `lst1`. The code uses logical and and or operators to select the list with the criteria mentioned in the prompt.