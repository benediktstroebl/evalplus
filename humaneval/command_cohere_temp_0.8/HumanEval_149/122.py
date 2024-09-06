```python
def sorted_list_sum(lst):
    lst = [x for x in lst if len(x) % 2 == 0]
    lst.sort(key=lambda x: (-len(x), x))
    return lst
```
This Python script defines a function called `sorted_list_sum` that takes a list of strings as input. It filters out any strings with odd lengths using a list comprehension, ensuring that the list only contains strings with even lengths. After that, it sorts the list using a lambda function with two key parameters: the first one reverses the sorting order based on the length of each string, and the second key sorts the strings alphabetically if they have the same length. The function then returns the sorted list of strings.