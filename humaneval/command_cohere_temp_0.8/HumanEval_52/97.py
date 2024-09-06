```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all` function to iterate over each element in the input list `l` and compare each element with the threshold value `t`. 

Here is an example of how to use the function:
```python
list_ = [1, 2, 4, 10]
threshold = 100
print(below_threshold(list_, threshold))
```
This will output:
```
True
```

The function will return `True` because all the values in the list are less than the threshold value of 100. 

If you change the values of the list to be greater than the threshold, the function will return `False`:
```python
list_ = [1, 20, 4, 10]
threshold = 5
print(below_threshold(list_, threshold))
```
This will output:
```
False
```

The function will return `False` because not all the values in the list are less than the threshold value of 5. 
It is important to note that the function will return a boolean value (`True` or `False`) depending on whether all elements in the list are less than the threshold value.