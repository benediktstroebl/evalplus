```python
def sorted_list_sum(lst):
    lst_result = []
    for e in lst:
        if len(e) % 2 == 0:
            lst_result.append(e)
    # sort the list alphabetically and by length
    lst_result.sort(key=lambda x: (len(x), x))
    return lst_result
```
The solution uses a simple loop to filter out strings with odd lengths and creates a new list `lst_result` that contains only even-length strings from the original list `lst`. Then the list is sorted by the length of each string first and alphabetically second. The function returns the `lst_result` list. 

This solution passes both tests presented in the problem statement.