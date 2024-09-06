```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each list element `x`, comparing it to the threshold `t` using the `<` operator. The `all()` function returns `True` if all comparisons are `True`, indicating that all numbers in the list are below the threshold, otherwise `False`. 
The function's docstring also indicates how to use the function and provides specific test cases, noting that the function should return `True` for the first example (`[1, 2, 4, 10], 100`) and `False` for the second (`[1, 20, 4, 10], 5`). Hiding 2 code blocks behind a spoiler alert since they contain repeated content:
```
```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
```
```python
>>> below_threshold([1, 2, 4, 10], 100)
True
>>> below_threshold([1, 20, 4, 10], 5)
False
```
```