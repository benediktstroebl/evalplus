```python
def sorted_list_sum(lst):
    lst = [x for x in lst if len(x) % 2 == 0]
    lst.sort(key=lambda x: (-len(x), x))
    return lst
```
This Python script provides a function called `sorted_list_sum` that takes a list of strings as input. This function first filters out any strings with odd lengths, creating a new list that contains only the even-length strings from the input list. It then sorts this filtered list using a custom sorting key, where strings are first sorted in descending order based on their length, and if two strings have the same length, they are sorted alphabetically in ascending order. The function finally returns this sorted list of even-length strings.