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
This Python script solves the problem in a way that first filters the list to include only strings that have even lengths, and then sorts the list and excludes the first element from the sort, which is the shortest element in the list, and therefore the list will only have the longest word with the same length. The function returns the resulting list. The script should be run with Python 3.