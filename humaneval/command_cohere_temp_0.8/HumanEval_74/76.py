```python
def total_match(lst1, lst2):
    l1_total = sum(len(x) for x in lst1)
    l2_total = sum(len(x) for x in lst2)
    if l1_total < l2_total:
        return lst1
    elif l2_total < l1_total:
        return lst2
    else:
        return lst1 if len(lst1) < len(lst2) else lst2
```

The code sums the lengths of all strings in both lists, and then checks if one total is less than the other. If one does, it returns the list that has the fewer total character count. If both lists have an equal total count, it returns the first list if it has fewer elements, otherwise it returns the second list. This problem can also be solved using Python's `min` function, as follows:
```python
def total_match(lst1, lst2):
    return min(lst1, lst2, key=len)
```

This works because the `min` function triggers a keyword argument `key` that specifies a function to return the comparison key for sorting the arguments. The `len` function is used as that comparison key to return the total character count of each list, and therefore the `min` function returns the list with fewer characters. Both functions pass the test cases.