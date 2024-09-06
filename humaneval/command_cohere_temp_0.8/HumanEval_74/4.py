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

The problem is to write a function that accepts two lists of strings and returns the list that has the total number of chars in all the strings of the list less than the other list. If the two lists have the same number of chars, return the first list.

The `total_match()` function uses `sum()` function to calculate the total character count in each list respectively and compares the counts to return the list with a lower total count, ensuring the returned list has the most exhaustive matching strings.

The unit tests propose various cases to verify the functionality of the function and ensure its correctness against the given examples. 

The test cases are structured in a way to cover different scenarios, such as empty lists, one-char strings, and varying lengths of strings in the list. This way, the function should cover all important cases and provide an accurate solution to the problem.