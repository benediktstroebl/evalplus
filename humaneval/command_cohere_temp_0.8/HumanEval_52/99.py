```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all` function to iterate over each element in the input list `l` and checks if each element is less than the given threshold `t`. 

The `below_threshold` function returns `True` if all elements in the list are below the threshold, otherwise it returns `False`.