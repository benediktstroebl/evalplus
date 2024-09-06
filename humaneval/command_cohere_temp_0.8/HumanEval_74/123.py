```python
def total_match(lst1, lst2):
    # calculate the total characters in all strings of the list
    total1 = sum(len(x) for x in lst1)
    total2 = sum(len(x) for x in lst2)
    
    # check if total1 is less than total2
    if total1 < total2:
        return lst1
    elif total2 < total1:
        return lst2
    else:
        # if total is same, return the first list
        return lst1
```

The function calculates the total number of characters in the strings of both input lists. This is done using the `sum()` function in combination with the `len()` function to get the length of each string in the list. 

If one list has more characters than the other, it is returned. If the two lists have the same number of characters, the first list is returned.

The `total_match()` function solves the problem as described in the prompt. It takes two lists as input and returns the list with the lower total number of characters in its strings. Or, it returns the first list if the two lists have the same number of characters. 

This solution assumes that the lists are of strings or can be converted to strings. `sum()` and `len()` work fine with strings as well as with numbers. 

Note: the function assumes that the members of the list are strings. If the members are not strings, the `sum()` and `len()` functions will raise a mistake. Therefore, if the members of the list are not strings, it should be added to either convert them to strings or handle the error.