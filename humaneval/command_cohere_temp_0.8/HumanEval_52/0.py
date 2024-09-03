```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all` function to iterate over each element in the input list `l` and compares each element with the threshold value `t`. 

Here is an example usage of the function:
```python
print(below_threshold([1, 2, 4, 10], 100))
```
The function will return `True` as all the numbers in the list are below the threshold value of 100. 

And here is another example usage of the function: 
```python
print(below_threshold([1, 20, 4, 10], 5))
```
The function will return `False` as not all the numbers in the list are below the threshold value of 5.