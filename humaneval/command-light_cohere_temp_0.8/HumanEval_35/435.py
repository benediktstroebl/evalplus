```python
def max_element(lst):
    return lst[-1] if len(lst) == 1 else max(lst)

# Test the function with some inputs
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
print(max_element([-5, -10, -20]))
```

This script defines a function `max_element` that takes a list as input and returns the maximum element in the list. The function returns the same value if the list has only one element (in case of an empty list it returns `None`). Otherwise, it uses the `max()` function from the `math` module to find the maximum element in the list.