```python
def below_threshold(l, t):
    return all(x < t for x in l)
```
This function uses the built-in `all` function to iterate over each element in the input list `l` and compare it to the threshold value `t`. It then returns `True` if all elements in the list are below the threshold, and `False` otherwise.

Here is a simple test case to ensure the function is operating correctly:
```python
assert below_threshold([1, 2, 4, 10], 100) is True
assert below_threshold([1, 20, 4, 10], 5) is False
``` 
This asserts that the function `below_threshold` returns the expected values for the given test cases.