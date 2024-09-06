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

The code uses `sum` along with `len` to calculate the total count of characters in `lst1` and `lst2` and leverages these counts to determine which list should be returned. If the char counts are the same, the function returns `lst1`, as per the problem's guidance. If the count is lesser in `lst1`, it returns `lst1`, and if the count is lesser in `lst2`, it returns `lst2`. However, if the counts are not equal and differ by only 1 (due to counting inclusivity of the sum operation), the result will incorrectly be `[]`, as the code doesn't account for this specific case. 

**NOTE:** The approach assumes that the lists are non-empty and that the strings within the lists have a length greater than 0. If either of these assumptions is violated (e.g., one of the lists is empty or a string within a list has a length of 0), the function may not behave as expected.