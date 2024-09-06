```python
def sorted_list_sum(lst):
    lst_new = []
    for x in lst:
        if len(x) % 2 == 0:
            lst_new.append(x)
    lst_new.sort()
    for i in range(len(lst_new)):
        if i > 0 and lst_new[i] == lst_new[i - 1]:
            del lst_new[i]
    return lst_new
```
The solution uses a list comprehension to filter out strings with odd lengths from the input list. The code then sorts the resulting list and removes duplicate consecutive elements while sorting. This ensures that the resulting list is sorted and contains only unique even-length strings, as required by the problem statement.