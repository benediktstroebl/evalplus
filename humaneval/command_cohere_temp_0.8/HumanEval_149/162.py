```python
def sorted_list_sum(lst):
    lst = [x for x in lst if len(x) % 2 == 0]
    lst.sort(key=lambda x: (len(x), x))
    return lst
```
This Python script defines a function called `sorted_list_sum` that takes a list of strings as input. It filters out any strings with odd lengths using a list comprehension, ensuring that the result contains only strings with even lengths. After filtering, the list is sorted using a lambda function, first by the length of each string and then, if the length is the same, in alphabetical order. The function returns the sorted list of strings. In the given example, it would return ["aa", "ab", "cd"], and for the second example, it would return ["aa", "aaa", "ab", "cd"].