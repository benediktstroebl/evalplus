```python
def total_match(lst1, lst2):
    return lst1 if len(lst1) == len(lst2) else len(lst1) < len(lst2) and lst1 or lst2
```
The `total_match` function uses the logic that the returned solution must be a list that has a total number of chars in all of their strings less than the other list. Hence, if the lists have the same number of characters, it returns the first list. The or operator is used to merge the lists relativity freely while maintaining the correctness of the solution.