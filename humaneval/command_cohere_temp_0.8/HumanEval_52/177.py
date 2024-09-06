```python
def below_threshold(l, t):
    return all(x < t for x in l)
```
This function uses the built-in `all` function to iterate over each element in the input list `l` and compare it to the threshold value `t`. The function returns `True` if all elements in the list are below the threshold, and `False` otherwise. 

Here is an example of how to use this function:
```python
>>> below_threshold([1, 2, 4, 10], 100)
True
>>> below_threshold([1, 20, 4, 10], 5)
False
```
This example has the same inputs as the ones in the original problem description, ensuring that the function `below_threshold` still produces the expected outputs.