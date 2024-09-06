```python
def below_threshold(l, t):
    return all(x < t for x in l)
```
This function uses the built-in `all` function to iterate over each item in the input list `l` and compare it to the threshold value `t`. The function then returns `True` if all items in the list are below the threshold, and `False` otherwise.

Here is a simple test case to verify the functionality of the function:
```python
assert below_threshold([1, 2, 4, 10], 100) is True
assert below_threshold([1, 20, 4, 10], 5) is False
``` 
This test suite demonstrates the behavior of the `below_threshold` function for multiple cases. Specifically, it verifies that all elements in the list `[1, 2, 4, 10]` are below the threshold value of `100`, and that not all elements in the list `[1, 20, 4, 10]` are below the threshold value of `5`.