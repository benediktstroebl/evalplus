```python
def below_threshold(l, t):
    return all(x < t for x in l)
```
The function `below_threshold` uses the built-in `all` function to iterate over all elements in the list `l` and checks if each element is less than the threshold `t`. 

You can test the function by calling it with different lists and thresholds to verify that it returns the expected boolean values.