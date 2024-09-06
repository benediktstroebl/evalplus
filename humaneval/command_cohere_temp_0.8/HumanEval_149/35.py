```python
def sorted_list_sum(lst):
    lst = [x for x in lst if len(x) % 2 == 0]
    lst.sort(key=lambda x: (-len(x), x))
    return lst
```
This Python script defines a function called `sorted_list_sum` that takes a list of strings as input. It filters out any strings with odd lengths using a list comprehension, ensuring that the list only contains strings with even lengths. After filtering, the list is sorted using a lambda function, first by reversing the length of each string and then alphabetically if the lengths are the same. The function returns the final sorted list of strings.