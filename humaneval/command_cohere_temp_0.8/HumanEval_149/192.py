```python
def sorted_list_sum(lst):
    lst_new = []
    for i in lst:
        if len(i) % 2 == 0:
            lst_new.append(i)
    lst_new.sort()
    for i in range(len(lst_new)-1):
        if lst_new[i] == lst_new[i+1]:
            lst_new[i+1] += lst_new[i]
    return lst_new
``` 

The method loops through the list and checks if the length of each element has an even int divisor, adding it to the new list if it does. The elements in the new list are then sorted and any duplicate elements are summed and added to the larger element to be considered as 1 element. The resulting list is then returned after these processes. 

```python
TEST_CASES = [
    ['aa', 'a', 'aaa', 'ab', 'c', 'aaa', 'bc', 'd'],
    [('aa', 'a'), ('aaa',), ('ab', 'c'), ('aaa', 'bc', 'd')],
    ['aa', 'a', 'aaa', 'ab', 'c', 'aaa', 'bc', 'd', 'ae'],
    ['xx', 'xx', 'xx', 'yy', 'yy', 'zz', 'zz', 'zz']
]

EXPECTED_RESULTS = [['aa', 'ab', 'aaa', 'c', 'aaa', 'bc', 'd'], ['aa', 'a', 'aaa', 'ab', 'c', 'cd', 'd'], ['aa', 'ab', 'aaa', 'c', 'aaa', 'bc', 'd', 'ae'], ['xx', 'yy', 'zz']]

for i, test_case in enumerate(TEST_CASES):
    try:
        assert sorted_list_sum(test_case) == EXPECTED_RESULTS[i]
    except:
        assert False
```