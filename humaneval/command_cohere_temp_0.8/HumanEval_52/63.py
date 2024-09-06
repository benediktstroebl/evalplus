```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each element in the input list `l` and compare each element with the threshold value `t`. 

Here is an example of how to use the function:
```python
>>> below_threshold([1, 2, 4, 10], 100)
True
>>> below_threshold([1, 20, 4, 10], 5)
False
```
This would return True and False, respectively, as expected.