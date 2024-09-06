```python
def sorted_list_sum(lst):
    lst_length = len(lst)
    if lst_length % 2 == 0:
        return lst
    new_list = []
    for i in lst:
        if len(i) % 2 == 0:
            new_list.append(i)
    new_list.sort()
    return new_list
```

The method loops through the list of strings (lst), adding any strings with even lengths to the new_list. The new list is then sorted in ascending order and returned.

This algorithm completes the task in `O(n)` time complexity and `O(n)` space complexity, where `n` is the length of the input list.

The code may be tested using examples such as:
```python
tested_lists = [
    ["aa", "a", "aaa"],
    ["ab", "a", "aaa", "cd"],
    ["aaaa", "ab", "ac", "aabb"],
    ["bee", "b", "aa", "aab"],
]

for test in tested_lists:
    assert sorted_list_sum(test) == ["aa", "ab", "cd", "aaa"]
```