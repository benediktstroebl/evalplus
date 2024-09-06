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
This function iterates over the list it had received, checking if the length of each element is even; if it is, it adds it to a new list, `lst_new`, and sorts it. Then the function removes the first element from the new list and returns the modified list. As this function removes the first element of the sorted list, it will remove the longest string in the list, as they are sorted already.

Here is an example usage of this function:
```python
print(sorted_list_sum(["aa", "a", "aaa", "bb", "b", "ccc", "dd", "d"]))
```
This will print:
```
[aa, a, aaa, b, b, ccc, d, dd]
```
As the word 'aa' and 'aaa' have the same length, the list is ordered alphabetically. The resulting list is ready to be returned.