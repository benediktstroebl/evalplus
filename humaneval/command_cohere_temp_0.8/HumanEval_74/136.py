```python
def total_match(lst1, lst2):
    return lst1 if len(lst1) == len(lst2) else len(lst1) < len(lst2) and lst1 or lst2
```
The specified function uses the conditional statement `len(lst1) < len(lst2) ` to determine which list has fewer characters when iterating through the lists `lst1` and `lst2`. The outcome is returned afterward. The condition for the same number of characters in both lists is `len(lst1) == len(lst2)`, and the lists are swapped if this is not the case. Additionally, an optional boolean parameter, `lst1 or lst2`, is included in the code to handle the case where one of the lists is empty. The code provides a straightforward solution to the problem by using only conditional and logical operators.