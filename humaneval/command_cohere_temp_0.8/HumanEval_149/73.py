```python
def sorted_list_sum(lst):
    lst_new = []
    for i in lst:
        if len(i) % 2 == 0:
            lst_new.append(i)
    lst_new.sort()
    for i in range(len(lst_new)-1):
        if lst_new[i] == lst_new[i+1]:
            lst_new[i+1] += lst_new[i]
    return lst_new
``` 

This Python script defines a function called `sorted_list_sum` which takes a list of strings as input. It filters out strings with odd lengths and then sorts the even-length strings and aggregates any duplicates. The function ultimately returns a list of strings in sorted order. 

This approach is testable and solves the problem statement, multiple test cases can be added to test different scenarios of the problem.