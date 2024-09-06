```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each list element `x`, comparing it to the threshold `t` using the `<` operator. The `all()` function returns `True` if all comparisons are `True`, indicating that all elements are below the threshold, otherwise `False`.  This behavior is correctly illustrated in the docstring:
```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
```python
>>> below_threshold([1, 2, 4, 10], 100)
True
>>> below_threshold([1, 20, 4, 10], 5)
False
``` 
Which accurately reflects the problem statement.