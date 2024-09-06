```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all` function to iterate over each item in the input list `l` and quickly compares each item to the threshold value `t`. It then returns `True` if all items are below the threshold, and `False` otherwise.