```python
def total_match(lst1, lst2):
    char_count_lst1 = sum(len(el) for el in lst1)
    char_count_lst2 = sum(len(el) for el in lst2)
    if char_count_lst1 == char_count_lst2:
        return lst1
    elif char_count_lst1 < char_count_lst2:
        return lst1
    elif char_count_lst1 > char_count_lst2:
        return lst2
    else:
        return []
```

The code uses `sum` along with `len` to get the total count of characters in the strings of both lists. If both lists have the same number of characters, it returns the first list. If one list has fewer characters, it returns the list with fewer characters, and if one list has more characters, it returns an empty list as per the problem's guidelines. 

The function's logic follows the instructions in the prompt about the return value when the character count is greater than or equal to the comparison list, specifically returning the other list in such cases. It is also important to note that this code assumes that both lists contain strings only. If any list contains a non-string element, the sum and len operations would raise an error, and the function would not return the expected results.