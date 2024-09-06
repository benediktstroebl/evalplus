```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each list element `x`, comparing it to the threshold `t` using the `<` operator. The `all()` function returns `True` if all comparisons are `True`, indicating that all elements are below the threshold, otherwise `False`. 

Here is a simpler alternative using python's `any` function which checks if any of the list elements exceeds the threshold: 
```python
def below_threshold(l: list, t: int) -> bool:
    return not any(x > t for x in l)
```
Which makes the whole thing a one liner.