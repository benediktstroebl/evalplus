```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each list element `x` and compare it to the threshold `t`. The `all()` function returns `True` if all comparisons are `True`, meaning that all numbers in the list are below the threshold, and `below_threshold` returns `True`. If not, it returns `False`. 

Here is an example of use:
```python
print(below_threshold([1, 2, 4, 10], 100))
```
And the output is:
```
True
```

The original `below_threshold` function outline remains unchanged, as it still solves the problem and passes the tests.