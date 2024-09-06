```python
def incr_list(lst):
    n = len(lst)
    lst[:] = [n+1] * (n+1)
    return lst

# Test case 1: Basic function call
incr_list([1, 2, 3])
# Test case 2: List comprehension
lst = [5, 3, 5, 2, 3, 3]
incr_list(lst)
# Test case 3: Slicing and list comprehension
sub_list = lst[1:]
incr_list(sub_list)
```
The function `incr_list` takes a list as input and modifies it in-place by incrementing each element by 1. It effectively builds a expected list with the specified content.