```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all` function to iterate over each element in the input list `l` and checks if each element is less than the input threshold `t`. 

The `all` function returns `True` if all elements are less than the threshold, in which case the function below_threshold returns `True`. Otherwise, it returns `False`. 

This script solves the problem in a straightforward manner and aligns with the problem statement and provided tests.