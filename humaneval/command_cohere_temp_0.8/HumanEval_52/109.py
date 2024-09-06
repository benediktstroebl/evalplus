```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each list element `x` and compare it to the threshold `t`. The `all()` function returns `True` if all comparisons are `True`, meaning that all elements of the list are below the threshold, and `below_threshold()` returns `True`. If any comparison is `False`, `all()` returns `False`, and `below_threshold()` returns `False`. 

Here is an example of usage:
```python
>>> below_threshold([1, 2, 4, 10], 100)
True
>>> below_threshold([1, 20, 4, 10], 5)
False
```
This example is consistent with the given specification.