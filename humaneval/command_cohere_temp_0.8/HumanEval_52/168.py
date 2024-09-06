```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all` function to iterate over each element in the input list `l` and compare each element with the threshold value `t`. 
The result is returned as a boolean indicating whether all elements are below the threshold `t` or not. 

Here is a example usage of the function:
```python
print(below_threshold([1, 2, 4, 10], 100))
print(below_threshold([1, 20, 4, 10], 5))
```
This will result in the following output:
```
True
False
```
Which matches the previously stated behavior.