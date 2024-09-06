```python
def below_threshold(l, t):
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each element in the input list `l` and compare each element with the threshold value `t`. 

Here is an example of how to use the function:
```python
print(below_threshold([1, 2, 4, 10], 100))
```
This will return:
```
True
```
The function will return `True` because all numbers in the list are below the threshold value of 100. 

Another example:
```python
print(below_threshold([1, 20, 4, 10], 5))
```
This will return:
```
False
```
The function will return `False` because not all numbers in the list are below the threshold value of 5.