```python
def sorted_list_sum(lst):
    lst = [e for e in lst if len(e) % 2 == 0]
    lst.sort(key=lambda x: (-len(x), x))
    return lst
```
This Python script defines a function called `sorted_list_sum` that takes a list of strings as input. It filters out any strings with odd lengths using a list comprehension, ensuring that the list only contains strings with even lengths. Then, it sorts the list using a tuple unpacking approach, where the key argument is a lambda function that sorts the list first based on the negative length of the string (so that longer strings come first) and then alphabetically in case of a tie. This ensures that the resulting list is sorted by length, and in case of a length tie, it's sorted alphabetically. The function then returns the sorted list of strings.