```python
def sorted_list_sum(lst):
    lst = [x for x in lst if len(x) % 2 == 0]
    lst.sort(key=lambda x: (len(x), x))
    return lst
```
This Python script defines a function called `sorted_list_sum` that takes a list of strings as input. It filters out any strings with odd lengths using a list comprehension, ensuring that the list only contains strings with even lengths. Then, it sorts the list using a lambda function with two key parameters: the length of the string and the actual string itself. This ensures that the resulting list is sorted first by string length and then alphabetically if the lengths are the same. The function returns the final sorted list of strings.