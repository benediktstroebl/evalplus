```python
def sorted_list_sum(lst):
    lst_new = []
    for i in lst:
        if len(i) % 2 == 0:
            lst_new.append(i)
    lst_new.sort()
    for i in range(len(lst_new)-1):
        if lst_new[i] == lst_new[i+1]:
            lst_new[i+1] = lst_new[i] + lst_new[i+1]
    return lst_new
```
This Python script provides a function called `sorted_list_sum`, which takes a list of strings as input. First, it filters out the strings with odd lengths, creating a new list containing only the even-length strings. It sorts this new list in ascending order based on the length of the strings. If two strings have the same length, it sorts them alphabetically. Finally, it returns the sorted list of even-length strings.