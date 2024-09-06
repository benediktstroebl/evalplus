```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each list element `x`, comparing it to the threshold `t`. If all `x` values are less than `t`, the function returns `True`, indicating that all elements in the list are below the threshold. If not, it returns `False`. 

Here is a test case to ensure the function behaves correctly:
```python
assert below_threshold([1, 2, 4, 10], 100), "Expected True, but got False"
assert not below_threshold([1, 20, 4, 10], 5), "Expected False, but got True"
```
This first test case checks that the function returns `True` when all elements in the list are below the threshold. The second test case checks that the function returns `False` when at least one element is larger than the threshold.