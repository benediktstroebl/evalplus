```python
def below_threshold(l, t):
    return all(x < t for x in l)
```
The function `below_threshold` uses the built-in `all` function to iterate over all elements in the list `l` and compare them to the threshold value `t`. It returns `True` if all elements in the list are below the threshold, and `False` otherwise.

Here is a simple test case to verify the functionality of the function:
```python
assert below_threshold([1, 2, 4, 10], 100) == True
```

And another test case to check its functionality for when the threshold is 5:
```python
assert below_threshold([1, 20, 4, 10], 5) == False
```

The expected return values for these test cases are True and False, respectively. 
The code snippet provided fully addresses the problem statement in a concise and elegant manner.