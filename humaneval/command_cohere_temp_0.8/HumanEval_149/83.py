```python
def sorted_list_sum(lst):
    lst = [x for x in lst if len(x) % 2 == 0]
    lst.sort(key=lambda x: (-len(x), x))
    return lst
```
This Python script defines a function called `sorted_list_sum` that takes a list of strings as input. It filters out any strings with odd lengths using a list comprehension, ensuring that the list only contains strings with even lengths. After that, it sorts the list using a lambda function with two key arguments.

The first key argument, `-len(x)`, sorts the list in ascending order based on the length of each string, with the shortest strings appearing first. The second key argument, `x`, sorts the strings with the same length alphabetically. This ensures that the resulting list is sorted by length and, within the same length, alphabetically.

The function returns the final list, which may contain duplicates, after this sorting process. Thus, it unconditionally returns the updated list, regardless of its initial content and size. You can use this function to sort a list of strings as per the given specification and ensure the list only includes strings with even lengths.