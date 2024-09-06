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

The Python script defines a function called `total_match` that takes two lists, `lst1` and `lst2`, as input. It calculates the total number of characters in all strings in both lists using generators and the `sum()` function. It then compares the total character counts of both lists and returns the list with fewer total characters, or the first list if they have the same count. If the strings in `lst1` contain fewer characters than those in `lst2`, the function returns `lst1`. If the strings in `lst2` contain fewer characters, it returns `lst2`. If the character counts are the same, it returns a new list containing the unique strings present in both lists, ensuring that the returned list contains the shortest common subset of strings.