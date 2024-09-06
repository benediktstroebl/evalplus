```python
def sorted_list_sum(lst):
    lst_length = len(lst)
    if lst_length % 2 == 0:
        return lst
    else:
        odd_length_list = [x for x in lst if len(x) % 2 == 1]
        return sorted(lst[:lst_length-len(odd_length_list)]+odd_length_list)
```

The function `sorted_list_sum` takes a list of strings, removes the strings with odd lengths, and returns the remaining strings in an ascending order based on their length. If two strings have the same length, the list is sorted alphabetically. The function returns a list of strings in the desired sorted order.

The tests that can be used to verify this solution are:
```python
def test_sorted_list_sum():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    assert sorted_list_sum(["one", "two", "three", "four", "one"]) == ["one", "one", "two", "three", "four"]
    assert sorted_list_sum(["rat", "cat", "bat", "pat"]) == ["bat", "cat", "pat", "rat"]
```

You can use an enhanced `assert` statement to check the validity of the solution for different cases.