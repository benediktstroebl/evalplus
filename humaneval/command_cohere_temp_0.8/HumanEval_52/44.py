```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all` function to iterate over each element in the input list `l` and compare each element with the threshold value `t`. 
Since the problem states that the return value of the function should be `True` if all the elements are below the threshold and `False` otherwise, the `all` function returns the desired value directly. 

This function solves the problem and passes the given tests.