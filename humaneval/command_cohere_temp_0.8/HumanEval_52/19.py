```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each list element `x`, comparing it to the threshold `t`. The `all()` function returns `True` if all comparisons are `True`, indicating that all list elements are below the threshold, otherwise `False`. 

Here is a simpler alternative using Python's built-in `any()` function, although it is not the most efficient one:
```python
def below_threshold(l: list, t: int) -> bool:
    return not any(x > t for x in l)
```
This alternative compares each element in the list to the threshold and uses the `not` operator to reverse the result of the `any()` function. If any of the elements exceed the threshold, the `any()` function will return `True`, and the `not` operator will return `False`, indicating that some elements are above the threshold. If none of the elements exceed the threshold, the `any()` function will return `False`, and the `not` operator will return `True`, indicating that all elements are below the threshold. 

Both functions are self-contained and solve the problem as requested, but the first function is more efficient as it leverages Python's `all()` function specifically designed for this use case while the second function uses the `any()` function, which checks for at least one true condition among the iterable.