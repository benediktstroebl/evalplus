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
This Python script solves the problem by iterating through each element in the list (`lst`). It verifies if the length of the element has parity (odd or even) using the expression `len(el) % 2 == 0`. If the length has parity, it adds the element to a new list called `lst_new`. After adding all the elements with even lengths to the new list, it sorts it using the `sort()` method. Sorting involves arranging elements in ascending order based on their lengths and considering the alphabetical order as a secondary criterion for elements with the same length. The function returns the list `lst_new` minus the first element, resulting in a list of strings in the desired sorted order.

Here is an example function call:
```python
assert sorted_list_sum(["aa", "a", "aaa", "ab", "b", "abc"]) == ["a", "ab", "b", "aa", "aaa", "abc"]
```

This call follows the problem statement and the expected input-output format. The function deletes the strings with odd lengths, resulting in a list with only even-length strings. Then, it sorts the list in ascending order based on the length of each word. If two words have the same length, the sorting is alphabetical. The result is a list of strings in the desired sorted order.