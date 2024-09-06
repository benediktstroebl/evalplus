```python
def sorted_list_sum(lst):
    lst_length = len(lst)
    if lst_length % 2 == 0:
        return lst
    else:
        strings_length = len(str(lst[0]))
        new_list = []
        for i in lst:
            if len(i) == strings_length:
                new_list.append(i)
        new_list.sort()
        return new_list
```

The approach for this solution is:
1. Check if the length of the list is even because if it is odd, that would mean there is at least one string of odd length in the list, and we would filter it out. Otherwise, we would just return the list as it is.
2. Assuming we are given a list where all strings have the same length, we would filter out the strings with that length from the list.
3. Sort the resulting list. Since we are sorting strings, after sorting we may have duplicates, so we filter the duplicates, and finally return the list.

The expected behavior for the tests would be:
```python
assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
```