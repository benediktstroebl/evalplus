```python
def below_threshold(l, t):
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each element in the input list `l`, and returns `True` if all elements are less than the threshold `t`. 

Here is a test case to ensure that the function runs correctly:
```python
assert below_threshold([1, 2, 4, 10], 100), "Expected True, but got False"
assert not below_threshold([1, 20, 4, 10], 5), "Expected False, but got True"
```

The function should return `True` for the first assertion because all numbers in the list `[1, 2, 4, 10]` are less than the threshold value of `100`. It should return `False` for the second assertion, as not all numbers in the list are less than the threshold value of `5`.