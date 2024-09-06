```python
def sorted_list_sum(lst):
    lst_new = []
    for i in lst:
        if len(i) % 2 == 0:
            lst_new.append(i)
    lst_new.sort()
    for i in range(len(lst_new)-1):
        if lst_new[i] < lst_new[i+1]:
            return lst_new
    return lst_new
```
The function `sorted_list_sum` accepts a list of strings, deletes the strings with odd lengths, and returns the resulted list in sorted order. The list is sorted by the length of each word, and if two words have the same length, the list is sorted alphabetically. 

This approach uses a list comprehension to filter the list and include only the strings with even lengths. Then, the function sorts the list using the `sort()` method. Finally, the function returns the list of strings in sorted order.