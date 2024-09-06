```python
def below_threshold(l, t):
    return all(x < t for x in l)
```
This function uses the built-in `all` function to iterate over each element in the input list `l` and compare it to the threshold value `t`. It then returns `True` if all elements in the list are below the threshold, and `False` otherwise.

Here is a test case to ensure that the function behaves correctly:
```python
assert below_threshold([1, 2, 4, 10], 100) == True
```

And another test case to check its behavior for when the condition is not met:
```python
assert below_threshold([1, 20, 4, 10], 5) == False
```

These test cases validate that the function works as required by the problem statement.