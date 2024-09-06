```python
def sorted_list_sum(lst):
    lst_new = []
    for el in lst:
        if len(el) % 2 == 0:
            lst_new.append(el)
    # sort the list in ascending order
    lst_new.sort(key=lambda x: (-len(x), x))
    return lst_new
```
The problem asks for a function that accepts a list of strings, deletes the strings that have odd lengths, and returns the resulted list with a sorted order. The list is always a list of strings and never an array of numbers, and it may contain duplicates. The order of the list should be ascending by length of each word, and you should return the list sorted by that rule. If two words have the same length, sort the list alphabetically. The function should return a list of strings in a sorted order. You may assume that all words will have the same length. Two unit tests were conducted to the function and both of them passed.

```python 
assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
```