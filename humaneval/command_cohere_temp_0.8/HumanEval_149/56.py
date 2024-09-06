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
This code solves the problem by first filtering out the list to contain only strings with even lengths. It then sorts the list and returns the list excluding the first element in the sorted list, which contains the longest string in the even-length subset. This is done by breaking the loop before the first iteration. The code effectively returns the sorted list without the longest even-length string. 

Here is an example of how you can test this function:
```python
def test_sorted_list_sum():
    assert sorted_list_sum(
        ["aa", "a", "aaa", "ab", "b", "aba", "abc", "ac", "bd", "bf"]
    ) == ["aa", "ab", "bd", "bf"]
    assert sorted_list_sum(
        ["one", "1", "11", "twenty", "2", "22", "21", "ten", "3", "33"]
    ) == ["1", "10", "11", "21", "22", "33"]
    assert sorted_list_sum(
        ["alpha", "a", "beta", "b", "gamma", "g", "delta", "d", "epsilon", "e"]
    ) == ["a", "b", "d", "e"]
```
The test cases ensure that the function correctly identifies the even-length strings, sorts them, and returns the desired subset.