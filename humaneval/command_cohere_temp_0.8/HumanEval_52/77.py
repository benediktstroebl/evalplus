```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each list element `x`, comparing it to the threshold `t` using the `<` operator. The `all()` function returns `True` if all comparisons are `True`, indicating that all elements are below the threshold, otherwise `False`.  This behavior is reflected in the example inputs provided in the prompt, where the function returns `True` for the first case and `False` for the second case. 
If the list is empty, the `all()` function will return `True` implicitly.