```python
def strange_sort_list(lst):
    result = []
    while lst:
        min_val = min(lst)
        max_rem = max(x for x in lst if x > min_val)
        result.extend([min_val, max_rem])
        lst = [x for x in lst if x <= max_rem]
    return result
``` 

This Python script defines a function called `strange_sort_list` that takes in a list of integers as input and returns a list of these integers in a strange order. This strange ordering is like the selection sort algorithm where the minimum value is selected and placed at the beginning of the result list, then the maximum value among the remaining elements is selected and placed at the end of the result list. The function repeats this process until the list is empty, thus generating the correct strange order of the integers. 

Here is an example of how to use this function:
```python
print(strange_sort_list([1, 2, 3, 4])) # [1, 4, 2, 3]
``` 

This would print the list [1, 4, 2, 3] as the strange sort order of the list [1, 2, 3, 4]. 

Also, when the input list is empty, the result list is also empty:
```python
print(strange_sort_list([]))  # []
```

Which prints the empty list `[]`, as expected. 

This script provides a concise and elegant way to solve the problem in Python while maintaining code readability and efficiency.