```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each element in the input list `l` and compare each element with the threshold value `t`. 
The result of this comparison is a boolean value, which is then returned by the function. 
If all elements in the list are less than the threshold, the result will be `True`, otherwise it will be `False`. 

This solution follows the given specification, as demonstrated by the tests provided in the original prompt. 

You can use this function by calling it and passing the list of numbers and the threshold value as arguments. 
For example:
```python
result = below_threshold([1, 2, 3, 4], 5)
print(result)  # Output: True
``` 

This will print `True` to the console, as all the numbers in the list `[1, 2, 3, 4]` are below the threshold value `5`.