```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all` function to iterate over each element in the input list `l` and compares each element with the threshold value `t`. 

Here is an example of how to use the function:
```python
>>> below_threshold([1, 2, 4, 10], 100)
True
>>> below_threshold([1, 20, 4, 10], 5)
False
```
This would return the values of True and False, respectively, since all elements in both lists are below the threshold value of 100 and only the first element is below the threshold value of 5.