```python
def total_match(lst1, lst2):
    l1,l2 = map(sum, (map(len, li) for li in (lst1, lst2))), len(lst2)
    return lst1 if l1 == l2 else lst2 if l1 > l2 else lst1
```
The code employs a tuple of two maps in order to attain the sum of lengths for both lists, which is necessary in order to make the comparison. If the sums of lengths are equal, the first list is returned, while if the sum of lengths of the second list is less than that of the first list, the second list is returned, and if the sum of lengths of the first list is less than that of the second list, the first list is returned, making certain that the total number of characters in the strings of one list is less than that of the other.

Here's the jupyter notebook with the corresponding test cases in order to check the correctness of the given solution:
```python
def total_match(lst1, lst2):
    l1,l2 = map(sum, (map(len, li) for li in (lst1, lst2))), len(lst2)
    return lst1 if l1 == l2 else lst2 if l1 > l2 else lst1
# Tests:
assert total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']
assert total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
assert total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']
assert total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']
assert total_match(['hi', 'admin'], ['hi', 'admin', 'project']) == ['hi', 'admin']
assert total_match(['hi', 'ad'], ['hi', 'ads', 'ad']) == ['hi', 'ads', 'ad']
```