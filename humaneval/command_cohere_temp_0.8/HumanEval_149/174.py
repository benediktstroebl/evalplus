```python
def sorted_list_sum(lst):
    lst_new = []
    for el in lst:
        if len(el) % 2 == 0:
            lst_new.append(el)
    lst_new.sort()
    for el in lst_new:
        if el != lst_new[0]:
            break
    return lst_new[:len(lst_new) - 1]
```
This function iterates over the list it had received, adding the elements to a new list if the length of the current element is even. The new list is then sorted, and the first element (if it's not the only element) is removed, assuming that it's a duplicate of the last element in the new list. The function then returns the new list, with the elements checked for having even lengths and sorted in ascending order. 

Here's a test to validate the function above:
```python
def test_sorted_list_sum():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    assert sorted_list_sum(["qq", "q", "qqq"]) == ["qq"]
    assert sorted_list_sum(["xx", "x", "xxx"]) == ["xx"]
    assert sorted_list_sum(["yy", "y", "yyy"]) == ["yy"]
    assert sorted_list_sum(["zz", "z", "zzz"]) == ["zz"]
```
The test contains multiple examples, each of which should be handled correctly by the function `sorted_list_sum`. 
If the function is correct, running this test will result in all assertions passing with no errors.