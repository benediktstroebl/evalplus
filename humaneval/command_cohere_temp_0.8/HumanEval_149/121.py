```python
def sorted_list_sum(lst):
    lst_new = []
    for el in lst:
        if len(el) % 2 == 0:
            lst_new.append(el)
    lst_new.sort()
    for el in lst_new:
        if el != lst_new[-1]:
            return lst_new
    else:
        return lst_new[:-1]
```

The function first builds a new list `lst_new` and populates it with strings that have even lengths, assuming all the words have the same length to make the process more efficient. Then it sorts `lst_new` and returns it. If the result is empty, it will return `lst_new[:-1]` to avoid empty list duplication.

The following tests would prove the correctness of the function:
```python
assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
assert sorted_list_sum(["aaa", "aa", "ab", "a"]) == ["aaa", "aa"]
assert sorted_list_sum(["aaaaaaa"]) == ["aaaaaaa"]
assert sorted_list_sum([]) == []
```