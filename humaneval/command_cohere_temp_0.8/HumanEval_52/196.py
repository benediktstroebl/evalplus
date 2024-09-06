```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each element in the input list `l` and compare each element with the threshold value `t`. 
Since the problem statement does not specify any particular order for the elements in the list, the `all()` function also ensures that the elements can be in any order – the threshold comparison will still work correctly.