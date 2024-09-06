```python
def sorted_list_sum(lst):
    lst = [x for x in lst if len(x) % 2 == 0]
    lst.sort(key=lambda x: (-len(x), x))
    return lst
```
This Python script defines a function called `sorted_list_sum` that takes a list of strings as input. It filters out any strings with odd lengths using a list comprehension, ensuring that the list only contains strings with even lengths. After filtering, the list is sorted using a lambda function with two key arguments: the first is the negative length of the string, which ensures that the sorting is in ascending order based on string length. If two strings have the same length, the second key argument alphasorts them in ascending order. Finally, the function returns the sorted list of strings.