```python
def sorted_list_sum(lst):
    lst = [str(el) for el in lst if el != '']
    lst.sort(key=lambda x: (len(x), x))
    return lst
```
This Python script defines a function called `sorted_list_sum` that takes a list of strings as input. Inside the function, it checks for empty strings and converts all elements to strings. Then, it sorts the list using a lambda function that first sorts by the length of each element and then, in case of a tie, sorts alphabetically. Finally, the function returns the sorted list of strings.