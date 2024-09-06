```python
def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(l)
```
The function `max_element` takes a list `l` as an argument and returns the maximum element in the list using the `max` function. The given examples in the docstring illustrate how the function works with different lists, returning either 3 or 123 as the maximum element respectively. 
The function seemingly solves the problem as required and passes the tests. It provides a self-contained solution without introducing any external dependencies or modifications to the codebase, which is already present in the Python standard library. 
If you would like to test the function you can try using it with different input lists to see the behavior. For example:
```python
print(max_element([10, 5, 50, 30, 20]))
```
Which will output:
```
50
``` 
as it's the largest element in the list.