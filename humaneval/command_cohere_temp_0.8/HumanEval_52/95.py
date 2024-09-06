```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all` function to iterate over each item in the input list `l` and compares it to the threshold value `t`. The `all` function returns `True` if all iterated values are true, and `False` otherwise. The output of the function is a boolean value that denotes whether all list elements are below the threshold, fulfilling the problem statement.