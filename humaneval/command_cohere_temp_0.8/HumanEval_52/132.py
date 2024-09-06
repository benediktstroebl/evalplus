```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all` function to iterate over each element in the input list `l` and compares each element with the threshold value `t`. 

Here is an example usage of the function:
```python
>>> below_threshold([1, 2, 4, 10], 100)
True
>>> below_threshold([1, 20, 4, 10], 5)
False
```
This example tests the function with two different scenarios and returns the appropriate boolean values. 

This function is self-contained and does not rely on any external variables or functions. It simply checks if all the numbers in the list are below the threshold, and returns `True` if they are, and `False` otherwise. 
```