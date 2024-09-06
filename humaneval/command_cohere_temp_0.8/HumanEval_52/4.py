```python
def below_threshold(l, t):
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each element in the input list `l`, and returns `True` if all elements are less than the threshold `t`. 

You can test this function by calling it with different lists and thresholds to verify that it returns the expected results.