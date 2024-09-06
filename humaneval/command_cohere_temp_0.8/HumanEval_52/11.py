```python
def below_threshold(l, t):
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each item in the input `list` `l`, and returns `True` if all items are less than the input `threshold` `t`. 

You can test this function with the provided example tests and additional tests you might want to add to verify it works as expected.