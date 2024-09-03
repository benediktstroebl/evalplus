```python
def total_match(lst1, lst2):
    char_count_lst1 = sum(len(x) for x in lst1)
    char_count_lst2 = sum(len(x) for x in lst2)
    if char_count_lst1 == char_count_lst2:
        return lst1
    elif char_count_lst1 < char_count_lst2:
        return lst1
    elif char_count_lst1 > char_count_lst2:
        return lst2
    else:
        return []
```

The code uses `sum` along with `len` to get the total character count of both lists. It then compares the counts and returns the appropriate list with fewer characters, or an empty list if the counts are equal. 

Here are some example outputs:
```
total_match(['hi', 'admin'], ['hI', 'Hi']) → ['hI', 'Hi']
total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) → ['hi', 'admin']
total_match(['4'], ['1', '2', '3', '4', '5']) → ['4']
``` 
If the lists have the same number of characters, the function returns the first list. If the character count of the second list is less than the first list, the function returns the second list. If the character count of the first list is less than the second list, the function returns the first list. Finally, if the character count of both lists is the same, and not equal to zero, the function returns an empty list.