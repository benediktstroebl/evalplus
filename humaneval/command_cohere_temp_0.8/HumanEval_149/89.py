```python
def sorted_list_sum(lst):
    lst_new = []
    for x in lst:
        if len(x) % 2 == 0:
            lst_new.append(x)
    lst_new.sort()
    for i in range(len(lst_new)):
        if i > 0 and lst_new[i] == lst_new[i - 1]:
            del lst_new[i]
    return lst_new
```
The algorithm uses a list comprehension to filter out the strings with odd lengths, then sorts the list, and finally removes any duplicate adjacent elements. The resulting list is returned. You can assert the function behaviour with the following tests:
```python
assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
```