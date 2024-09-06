```python
def sorted_list_sum(lst):
    lst = [x for x in lst if len(x) % 2 == 0]
    lst.sort(key=lambda x: (-len(x), x))
    return lst
```
This Python script defines a function called `sorted_list_sum` that takes a list of strings as input. It filters out any strings with odd lengths, resulting in a list of strings with even lengths. Then, it sorts the list based on the length of each string in descending order and uses the alphabetic sort as a secondary sorting criteria for strings with the same length. Finally, it returns the sorted list of strings. This function addresses the specified challenge of handling a list of strings with odd-length elements removed and returning a sorted list. 

The use of the `key` parameter in the `sort` function is an elegant way to handle the dual sorting criteria, which provides a concise and efficient solution to the problem.