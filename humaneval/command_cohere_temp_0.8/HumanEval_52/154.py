```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each element in the input list `l` and compare each element with the threshold value `t`. 
Since the problem statement does not specify any particular order for the elements in the list, the `all()` function also doesn't guarantee the order in which it checks the conditions.

Such a function should return `True` if all elements in the list are less than the threshold and `False` otherwise.