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
The method utilizes a 'list comprehension' and the 'sort' function to solve the problem. The expression '[i for i in lst if len(i) % 2 == 0]' creates a new list that contains every element in 'lst' that has an even length. Then the 'sort' function is applied on the new list, and finally, the function returns the sorted list.