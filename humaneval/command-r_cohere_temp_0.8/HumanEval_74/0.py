```python
def total_match(lst1, lst2):
    '''
    Returns the list with the total number of characters in all strings less than the other list.
    
    If the lists have the same total number of characters, the first list is returned.
    '''
    total_chars_lst1 = sum([len(x) for x in lst1])
    total_chars_lst2 = sum([len(x) for x in lst2])
    
    if total_chars_lst1 < total_chars_lst2:
        return lst1
    else:
        return lst2
```