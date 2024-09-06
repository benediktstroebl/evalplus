```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each element in the input list `l` and compares each element with the threshold value `t`.  If all elements are less than `t`, the function returns `True`, otherwise it returns `False`.  This behavior is explicitly tested in the provided tests, ensuring its accuracy. 
```python
>>> below_threshold([1, 2, 4, 10], 100)
True
>>> below_threshold([1, 20, 4, 10], 5)
False
``` 
This example provides return values that align with the problem description.