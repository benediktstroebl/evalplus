```python
def below_threshold(l, t):
    return all(x < t for x in l)
```
The function `below_threshold` uses the built-in `all` function to iterate over all elements in the input list `l` and checks if all elements are less than the given threshold `t`.  For each element `x` in the list `l`, the expression `x < t` is evaluated, and the `all` function returns `True` only if all expressions are `True`, meaning that all elements in the list are below the threshold, otherwise it returns `False`. 

This solution is concise and straightforward and should be able to handle the specified test cases. 
To test this function, you can call it with different lists and thresholds and check if it returns the expected results. 

For example:
```python
print(below_threshold([1, 2, 4, 10], 100)) # Output: True
print(below_threshold([1, 20, 4, 10], 5)) # Output: False
```

This should return `True` in the first case because all numbers in the list are below the threshold value of 100. In the second case, the result is `False` because the list contains numbers greater than 5, the given threshold.