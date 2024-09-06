```python
def below_threshold(l, t):
    return all(x < t for x in l)
```
The function `below_threshold` uses the built-in Python function `all` to return True if all elements in the list `l` are less than the threshold `t`. 

Here is an example of how this function can be tested:
```python
>>> below_threshold([1, 2, 4, 10], 100)
True
>>> below_threshold([1, 20, 4, 10], 5)
False
```
These tests evaluate the function with two different inputs and confirm that it returns the expected True and False results. 

The expected behaviour of the function is outlined in the docstring, which the function inherits from the built-in `all` function. 
```
True if all elements in the list are less than the threshold
``` 

Let me know if you would like me to explain any part of the code snippet in more detail.