```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each list element `x`, comparing it to the threshold `t` using the `<` operator. The `all()` function returns `True` if all comparisons are `True`, indicating that all numbers in the list are below the threshold, otherwise `False`. 

Here is a simpler alternative using Python's list comprehension: 
```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
In this version, the `all()` function is used with a generator expression to create a boolean list from each entry in the input list `l`, by comparing `x` to the threshold `t`. The `all()` function then returns `True` if all comparisons are `True`, signifying that all numbers in the list are below the threshold, and `False` otherwise. 

Both approaches are valid, but the latter uses a list comprehension, which some developers might find more readable.