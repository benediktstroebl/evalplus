```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all` function to iterate over each item in the input list `l` and checks if each item is less than the input threshold `t`. 

The `all` function returns `True` if all elements of the iterable are true, so in case all elements of the list are less than the threshold, the function returns `True`. Otherwise, returns `False`. 

You can test this function by calling it with different input lists and thresholds to verify its correctness against the given tests.