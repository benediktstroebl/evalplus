```python
def total_match(lst1, lst2):
    char_count_lst1 = sum(len(x) for x in lst1)
    char_count_lst2 = sum(len(x) for x in lst2)
    if char_count_lst1 == char_count_lst2:
        return lst1
    elif char_count_lst1 < char_count_lst2:
        return lst1
    else:
        return lst2
```

The code exploits the fact that the sum of the char lengths of all strings in both lists is the same or less than the char count in the `lst1` and greater in the `lst2`, which allows the code to simply return the list with the least char count without unnecessary complexities.