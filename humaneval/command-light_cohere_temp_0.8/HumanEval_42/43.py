```python
def incr_list(lst):
    n = len(lst)
    lst[::n + 1] = lst[::n] + 1
    return lst

# Test the function
lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assertEqual(incr_list(lst), [6, 4, 6, 3, 4, 4, 10, 1, 124])
```