```python
def sorted_list_sum(lst):
    lst = [x for x in lst if len(x) % 2 == 0]
    # Sorting the list in ascending order
    lst.sort(key=lambda x: (len(x), x))
    return lst
```
The `sorted_list_sum` function first uses a list comprehension to filter out the strings with odd lengths from the input list. Then it sorts the list in two steps: first by the length of each string (`len(x)`) and then by the string itself (`x`), which ensures that if two strings have the same length, they will be sorted alphabetically. The function returns the final sorted list.

#### Testing:
```python
def test_list_sort():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    assert sorted_list_sum(["ax", "ya", "yy", "xa"]) == ["ax", "xa"]
    assert sorted_list_sum(["thequickbrownfox", "fox", "dog", "cat"]) == ["cat", "dog", "fox", "thequickbrownfox"]
    assert sorted_list_sum(["hello", "world", "code", "ava"]) == ["ava", "code", "hello", "world"]
```