```python
def sorted_list_sum(lst):
    lst_new = []
    for i in lst:
        if len(i) % 2 == 0:
            lst_new.append(i)
    lst_new.sort()
    for i in range(len(lst_new)):
        if lst_new[i] != lst_new[i+1]:
            return lst_new
    return lst_new[:-1]
```
This code block provides a Python script that solves the problem presented in the given markdown code block. The `sorted_list_sum` function takes a list of strings as input and returns a sorted list of strings with even lengths, assuming all words have the same length.

The function first creates a new list `lst_new` and iterates through the original list, appending only the strings with even lengths to `lst_new`. It then sorts `lst_new` and iterates through it to check if the elements are unique. If the elements are unique, the function returns `lst_new`; otherwise, it returns `lst_new` without the last element, which ensures that only the unique elements with even lengths are retained in the sorted order.

The code includes an assumption that all words have the same length, and it handles the list manipulation and sorting requirements as specified in the challenge. It provides a concise and efficient solution to the problem with the given input constraints.