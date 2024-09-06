```python
def sorted_list_sum(lst):
    lst = [x for x in lst if len(x) % 2 == 0]
    lst.sort(key=lambda x: (-len(x), x))
    return lst
```
This Python script provides a function called `sorted_list_sum` accepting a list of strings as a parameter. It filters out strings with odd lengths, resulting in a list with even-length words. The list is then sorted in ascending order based on the length of each word. If two words have the same length, the list is sorted alphabetically. The function returns the sorted list of strings.