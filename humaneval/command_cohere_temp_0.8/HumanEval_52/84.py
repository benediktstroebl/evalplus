```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each list element `x` and compare it to the threshold `t`. The `all()` function returns `True` if all comparisons are `True`, meaning that all numbers in the list are below the threshold, and `below_threshold()` returns `True`. Otherwise, if any comparison is `False`, `all()` returns `False`, and `below_threshold()` returns `False`. The function's documentation includes two examples that illustrate its behavior for different inputs.