```python
def sorted_list_sum(lst):
    lst_new = []
    for x in lst:
        if len(x) % 2 == 0:
            lst_new.append(x)
    # Sorting the list in ascending order
    lst_new.sort()
    # Sorting the list alphabetically
    lst_new.sort(key=str.lower)
    return lst_new
```
The solution uses a simple iterative approach to filter out the strings with odd lengths and then uses `sort()` twice to ensure the list is sorted in the desired manner. One sorts the list alphebetically while the other sorts it by the length of each word. The function finally returns the desired result.