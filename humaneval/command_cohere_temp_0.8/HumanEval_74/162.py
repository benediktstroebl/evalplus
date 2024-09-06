```python
def total_match(lst1, lst2):
    return lst1 if len(lst1) == len(lst2) else len(lst1) < len(lst2) and lst1 or lst2
```
This function compares the total number of characters in two lists of strings and returns the list with fewer characters, or returns the first list if the two lists have the same number of characters. The function includes edge cases for empty lists, lists with one element, and lists with multiple elements.