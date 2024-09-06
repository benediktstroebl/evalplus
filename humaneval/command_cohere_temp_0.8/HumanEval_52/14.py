```python
def below_threshold(l, t):
    return all(x < t for x in l)
```
The function `below_threshold` uses the built-in `all` function to iterate over all elements in the input list `l` and compares them to the threshold value `t`. It then returns `True` if all elements in the list are below the threshold, and `False` otherwise.