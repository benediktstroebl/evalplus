```python
def total_match(lst1, lst2):
    l1_total = sum(len(x) for x in lst1)
    l2_total = sum(len(x) for x in lst2)
    if l1_total < l2_total:
        return lst1
    elif l2_total < l1_total:
        return lst2
    else:
        return [x for x in lst1 if x in lst2]
```

The problem is to write a function that accepts two lists of strings and returns the list that has the total number of chars in all strings of the list less than the other list. If the two lists have the same number of chars, return the first list.

The Python script defines a function called `total_match` taking two lists, `lst1` and `lst2`, as input. It calculates the total character count in each list using generators and the `sum()` function. The function then compares the total character counts of both lists and returns the list with fewer total characters, accordingly. If both lists have the same number of characters, the function returns the first list (`lst1`) as specified in the problem statement. The function finally uses a list comprehension to return the common elements of the lists if they have the same character count.