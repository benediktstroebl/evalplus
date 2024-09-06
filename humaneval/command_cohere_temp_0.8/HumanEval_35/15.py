```python
def max_element(l: list) -> int:
    """Returns the maximum element in the list."""
    return max(l)
``` 

This code defines a function called `max_element` that takes a list `l` as input and returns the maximum element in the list using the `max` function. 

The function is self-contained and can be run independently, as demonstrated by the docstring. 

It passes the given tests, as it returns the expected maximum value for both input lists. 
```python
>>> max_element([1, 2, 3])
3
>>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
123
``` 
If you run the above code, it will output:
```
3
123
``` 
The first output is the result of running the first test case, and the second output is from running the second test case. 

This code demonstrates how to solve the problem of finding the maximum element in a list using a self-contained Python function.