```python
def max_element(l: list) -> int:
    """Returns the maximum element in the list."""
    return max(l)
``` 

This code defines a function called `max_element` that takes a list `l` as input and returns the maximum element in the list. The function uses the `max` function, also known as the `built-in function` that returns the maximum value from a given list or tuple. 

In the case of a tie (when multiple elements in the list have the same maximum value), the function will return the first instance of that element encountered in the list. It is worth noting that this behavior matches the default behavior of the built-in `max` function in Python.