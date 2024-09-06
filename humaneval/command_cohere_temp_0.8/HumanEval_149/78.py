```python
def sorted_list_sum(lst):
    lst_new = []
    for x in lst:
        if len(x) % 2 == 0:
            lst_new.append(x)
    # Sorting the list in ascending order
    lst_new.sort()
    # Sorting the list in alphabetical order
    lst_new.sort(key=str.lower)
    return lst_new
```
The Python script solves the problem using the 'sorted_list_sum' function that takes a list of strings, filters strings with odd lengths, and returns the sorted results. The function first creates a new list 'lst_new' and populates it with strings having even lengths from the input list 'lst'. The code then sorts the new list first in ascending order based on the string lengths, and then in alphabetical order using the 'str.lower' sorting key, which ensures that strings with the same length are sorted alphabetically. Finally, the function returns the sorted list of strings.

Here is an example function call:
```python
assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
```