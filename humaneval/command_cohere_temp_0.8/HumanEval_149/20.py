```python
def sorted_list_sum(lst):
    lst = [item for item in lst if len(item) % 2 == 0]
    lst.sort(key=lambda x: (-len(x), x))
    return lst
```
This Python script defines a function called `sorted_list_sum` that takes a list of strings as input. It filters out any strings with odd lengths using a list comprehension, ensuring that the list contains only strings with even lengths. Then, it sorts the list using a lambda function with two key parameters: the first is the length of each string, and the second is a secondary key that sorts the strings alphabetically if their lengths are the same. The list is sorted in ascending order based on its length, and any ties are broken alphabetically. Finally, the function returns the sorted list of strings.