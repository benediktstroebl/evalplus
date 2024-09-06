```python
def max_element(l: list) -> int:
    """Return maximum element in the list."""
    return max(l)
``` 

This code defines a function called `max_element` that takes a list `l` as input and returns the maximum element in the list. The `max` built-in function is used to find the maximum value in the list. 

The docstring at the top of the function explains the purpose of the function, and the commented-out test cases below demonstrate the behaviour of the function for different inputs.

If we were to run this function with the help of the `max` function, the resultant code will be as follows:
```python
def max_element(l: list) -> int:
    return max(l)
``` 

And the usage of this function will be:
```python
max_element([1, 2, 3]) # 3
max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) # 123
``` 
The tests demonstrate that the function returns the expected maximum element for different input lists, confirming its usefulness.