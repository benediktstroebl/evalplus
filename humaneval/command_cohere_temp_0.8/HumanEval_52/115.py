```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each list element `x`, comparing it to the threshold `t` using the `<` operator. The `all()` function returns `True` if all comparisons are `True`, indicating that all elements are below the threshold, otherwise `False`.  This behavior is reflected in the example inputs provided in the problem statement, where the function is expected to return `True` in the first case and `False` in the second. 
To ensure completeness, this code snippet defines the function `below_threshold()` as requested, but it does not include any test cases within the script since they are already provided in the problem statement.