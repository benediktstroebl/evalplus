```python
def max_element(lst):
    if not_greater(lst) == None:
        return lst
    return max(lst, key=not_greater)

def not_greater(lst):
    return max(map(lambda x: x > lst[0], lst))
```
The function `max_element` takes a list as an argument and uses a helper function `not_greater` to compare each element with the first element of the input list, and returns the list of truthy elements from the list. The `not_greater` function uses the `max` function and a lambda function to compare each element with the first element of the list, and returns the list of truthy elements.