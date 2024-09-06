```python
def total_match(lst1, lst2):
    char_count_1 = sum(len(x) for x in lst1)
    char_count_2 = sum(len(x) for x in lst2)
    if char_count_1 > char_count_2:
        return lst1
    elif char_count_2 > char_count_1:
        return lst2
    else:
        return lst1 if len(lst1) < len(lst2) else lst2
```

The algorithm to solve this problem is straightforward. We sum the total characters in both lists first, and then compare the sums. From the sum, we can determine the list with fewer characters or the same list in case of a tie. We use len(lst1) < len(lst2) to prefer the list with fewer elements in case of a tie. The result is passed to the function as a list.