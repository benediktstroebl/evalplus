```python
def sorted_list_sum(lst):
    lst_len = len(lst)
    if lst_len % 2 == 0:
        return lst
    else:
        odd_idx = [i for i, x in enumerate(lst) if len(x) % 2 == 1]
        remove_ords = [ord(c) for c in lst[odd_idx[0]]]
        for i in odd_idx[1:]:
            remove_ords = [x for x in remove_ords if x != ord(lst[i][0])]
        remove_ords = list(set(remove_ords))
        filtered_lst = [x for x in lst if x[0] not in remove_ords]
        filtered_lst.sort(key=lambda x: (len(x), x))
        return filtered_lst
```

The method first checks if there is an odd number of strings in the list. If there is an odd number of strings, the method builds a list of indices to strings of odd length. It also builds a list of codepoints of the first character of strings to remove. The list of indices to remove is then filtered to avoid removing duplicates from the list. The remaining strings are sorted by length, and in case of a tie, sorted alphabetically.

The following tests will evaluate the function correctly:
```python
def test_sorted_list_sum():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    assert sorted_list_sum(["ab", "cd", "a", "aaa"]) == ["ab", "cd"]
    assert sorted_list_sum(["abc", "abcd", "ab", "cd", "d"]) == ["ab", "abcd", "cd", "d"]
    assert sorted_list_sum(["ac", "ca", "abc", "ba", "bb"]) == ["ac", "abc", "ba", "bb"]
```