```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each list element `x` and compare it to the threshold `t`. The `all()` function returns `True` if all comparisons are `True`, meaning that all numbers in the list are below the threshold, and `below_threshold()` returns `True`. If not, it returns `False`. 

Here is an example of use, which has been added to test whether the numbers in the list `[1, 2, 4, 10]` are below the threshold `100`:
```python
>>> below_threshold([1, 2, 4, 10], 100)
True
```
This example test is passing, as intended.