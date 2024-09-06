```python
def total_match(lst1, lst2):
    char_count_list1 = sum(len(x) for x in lst1)
    char_count_list2 = sum(len(x) for x in lst2)
    if char_count_list1 == char_count_list2:
        return lst1 if lst1 == lst2 else lst2 
    return lst1 if char_count_list1 < char_count_list2 else lst2
```

The algorithm to solve this problem:
- Calculate the total character length of both lists with summations.
- If both lists have an equal count, return either list (or deduplicate them).
- Return the list with fewer characters.

This algorithm optimizes the list sorting process, only using simple summations to compare list size.