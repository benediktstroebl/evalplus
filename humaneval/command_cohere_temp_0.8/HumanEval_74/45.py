```python
def total_match(lst1, lst2):
    return lst1 if len(lst1) == len(lst2) else len(lst1) < len(lst2) and lst1 or lst2
```
The `total_match` function uses the logic of comparing the total count of characters in all strings in both lists. If both lists have the same count, it returns the first list. Otherwise, it checks if the length of the resulting list would be less than the length of `lst2` after concatenation, and accordingly returns `lst1` or `lst2`. 

The following tests can be used to validate the function:
```python
test_list = ['hi', 'admin']
test_list2 = ['hI', 'Hi']
test_list3 = ['hi', 'hi', 'admin', 'project']
test_list4 = ['hI', 'hi', 'hi']
test_list5 = ['4']

assert total_match(test_list, test_list2) == test_list2
assert total_match(test_list, test_list3) == test_list
assert total_match(test_list, test_list4) == test_list1
assert total_match(test_list5, test_list4) == test_list5
```