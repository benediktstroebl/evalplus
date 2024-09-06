```python
def below_threshold(l, t):
    return all(x < t for x in l)
```
The function `below_threshold` uses the built-in Python function `all` to iterate over each element in the input list `l` and compare it to the threshold value `t`. The function returns `True` if all elements in the list are below the threshold, and `False` otherwise.

Here is a simple test case to validate the functionality of the function:
```python
assert below_threshold([1, 2, 4, 10], 100) is True
assert below_threshold([1, 20, 4, 10], 5) is False
```

This test case demonstrates that the function correctly identifies whether the list of numbers is entirely below the given threshold, and returns `True` if so, and `False` otherwise. 
The function's docstring also provides useful information to understand the expected inputs and the function's behavior.