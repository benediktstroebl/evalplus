```python
def sorted_list_sum(lst):
    lst = [x for x in lst if len(x) % 2 == 0]
    # sort by len() and alphabetically
    lst.sort(key=lambda x: (len(x), x))
    return lst
```
This Python script defines a function called `sorted_list_sum` that takes a list of strings as input. Here's what the function does:
1. It filters out any strings from the input list that have odd lengths using a list comprehension. After this step, the list will only contain strings with even lengths.
2. It then sorts the list based on two criteria: first by the length of each string, and if the lengths are the same, it sorts alphabetically. The `key` argument in the `sort` method is used with a lambda function `(lambda x: (len(x), x))` to specify this custom sorting order.

The function then returns the sorted list of strings.