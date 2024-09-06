```python
def total_match(lst1, lst2):
    char_count_1 = sum(len(item) for item in lst1)
    char_count_2 = sum(len(item) for item in lst2)
    if char_count_1 == char_count_2:
        return lst1
    elif char_count_1 < char_count_2:
        return lst2
    else: 
        return lst1
```
The code employs a `sum` function to calculate the total number of characters in `lst1` and `lst2`, ensuring the compatibility of the approach with the string type. The function returns the list with fewer characters, or, if both have the same count, the first list. 

This algorithm exhibits a time complexity of O(n) since it requires iterating through both lists only once to compute the total character count of each, making it an efficient solution.